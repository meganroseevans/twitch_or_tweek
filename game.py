import streamlit as st
import pandas as pd
import random
import requests
import re
import hashlib

@st.cache_data
def check_url_health(url):
    try:
        r = requests.head(url, timeout=5)
        return r.status_code == 200
    except requests.RequestException:
        return False

@st.cache_data
def load_image_data(region):
    return pd.read_csv(f'data/images/{region.lower()}_images.csv')

@st.cache_data
def load_audio_data(region):
    try:
        return pd.read_csv(f'data/audio/{region.lower()}_audio.csv')
    except OSError:
        return pd.DataFrame(columns=['name','audio_id','cc'])
    
@st.cache_data
def get_image_url(image_id):
    return f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{image_id}/900'

@st.cache_data
def get_audio_url(audio_id):
    return f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{audio_id}'

class BirdGame:
    def __init__(self, bird_image_df, bird_audio_df):
        """Initialise game state"""
        self.set_config()
        self.bird_image_df = bird_image_df
        self.bird_audio_df = bird_audio_df
        self.score = 0
        self.guesses = 0
        self.region = 'AU'
        self.mode = '2 :duck: intermediate'
        self.selection = None
        self.target_bird_name, self.target_bird_image, self.target_image_cc, self.multichoice_options, self.correct_bird_index = self.start_new_round()
        self.target_bird_audio = None
        self.target_audio_cc = None
        self.buttons = [self.multichoice_options]

    def set_config(self):
        st.set_page_config(
            page_title='Twitch or Tweek',
            page_icon='🦉',
            initial_sidebar_state='expanded'
        )

    def get_target_bird(self):
        """Select a bird at random"""
        selected_bird = self.bird_image_df.sample().iloc[0]
        return selected_bird['name'], selected_bird['image_id'], selected_bird['cc'], selected_bird['category']

    def get_audio_for_target_bird(self):
        bird_audio_files = self.bird_audio_df[self.bird_audio_df.name == self.target_bird_name][['audio_id','cc']]
        if bird_audio_files.shape[0] > 0:
            audio_file = bird_audio_files.sample(1)
            return audio_file.audio_id.iloc[0], audio_file.cc.iloc[0]
        else:
            return None, None

    def show_copyright(self, hyperlink, media_type, media_cc):
        st.markdown(f'''
            <a href="https://macaulaylibrary.org/asset/{hyperlink}" 
               style="color:#cf8865;font-family:courier;font-size:80%">
               {media_type} © {media_cc}
            </a>
            ''',
            unsafe_allow_html=True)

    def get_multichoice_options(self, target_bird_category):
        """Return list of bird names for multichoice button labels, based on game difficulty."""

        full_bird_list = [re.sub(r'\s\(.+\)','',x) for x in self.bird_image_df.name]
        short_bird_list = [re.sub(r'\s\(.+\)','',x) for x in self.bird_image_df.name[self.bird_image_df.category == target_bird_category]]

        # Set multichoice options based on game difficulty
        if self.mode[0] == '1':
            num_options = 2
            non_target_birds = [x for x in set(full_bird_list) if self.target_bird_name not in x]            
        elif self.mode[0] == '3':
            num_options = 4
            non_target_birds = [x for x in set(short_bird_list) if x != self.target_bird_name]
        elif self.mode[0] == '4':
            num_options = 5
            non_target_birds = [x for x in set(short_bird_list) if x != self.target_bird_name]
        else:
            num_options = 3
            non_target_birds = [x for x in set(full_bird_list) if self.target_bird_name not in x]

        # Select random sample of bird names for button labels
        multichoice_options = [self.target_bird_name] + random.sample(non_target_birds, min(num_options, len(non_target_birds)))
        random.shuffle(multichoice_options)

        # Register button index containing target bird
        correct_bird_index = multichoice_options.index(self.target_bird_name)

        return multichoice_options, correct_bird_index

    def start_new_round(self):
        """Select a new bird and multichoice options. Reset 'selection' to None.
        
        returns:
            - target_bird_name (str): name of bird to display
            - target_bird_image (str): ID of image to display
            - target_image_cc (str): copyright person
            - multichoice_options (list): multichoice button labels of bird names
            - correct_bird_index (int): index in multichoice list of target bird 
        """
        self.target_bird_name, self.target_bird_image, self.target_image_cc, self.target_bird_category = self.get_target_bird()
        self.multichoice_options, self.correct_bird_index = self.get_multichoice_options(self.target_bird_category)

        self.target_bird_audio, self.target_audio_cc = self.get_audio_for_target_bird()
        # Restart if options are too few
        if len(self.multichoice_options) < int(float(self.mode.split(' ')[0])) + 1:
            self.start_new_round()

        return self.target_bird_name, self.target_bird_image, self.target_image_cc, self.multichoice_options, self.correct_bird_index

    def post_score_results(self, selected_index):
        """Update score and play animations based on user's answer"""
        self.guesses += 1
        if self.correct_bird_index == selected_index:
            st.balloons()
            self.score += 1
        elif self.correct_bird_index != selected_index:
            st.snow()

    def display_multichoice(self):
        """Create multichoice buttons to display in right column"""
        for i, button_label in enumerate(self.multichoice_options):
            st.button(button_label, key=i, on_click=lambda i=i: self.register_selection(i))

    def register_selection(self, i):
        self.selection = i
    
    def deregister_selection(self):
        self.selection = None

    def display_ui(self):
        """Display the game interface: images, audio, buttons, text."""
        # Create two columns for side-by-side image and buttons
        media_column, buttons_column = st.columns([2, 1])

        # Display media
        with media_column:
            bird_image = get_image_url(self.target_bird_image)
            self.check_image_health(bird_image)
            st.image(bird_image)
            
            if str(self.target_image_cc) != 'nan':
                self.show_copyright(self.target_bird_image,'Image',self.target_image_cc)

            bird_sound = get_audio_url(self.target_bird_audio)
            audio_health = self.check_audio_health(bird_sound)
            if audio_health:
                st.audio(bird_sound)
                self.show_copyright(self.target_bird_audio,'Audio',self.target_audio_cc)
            else:
                st.write('🔇 Audio not available')                


        # Pre-selection show multichoice buttons. Post-selection show bird name and 'Next'.
        with buttons_column:
            if self.selection is not None:
                st.write(f'This is a {self.target_bird_name}')
                st.button('Next', on_click=self.deregister_selection)
            else:
                self.display_multichoice()

    def check_image_health(self, image_url):
        """Skip unhealthy/missing image by triggering a new round"""
        if not check_url_health(image_url):
            self.start_new_round()

    def check_audio_health(self, audio_url):
        """Return health status of audio file"""
        return check_url_health(audio_url)

def play_game(bird_game):
    """Play Twitch or Tweek"""

    # Display region select
    region_previous = bird_game.region
    bird_game.region = st.sidebar.selectbox('Region:',options=['AU','CA','GB','JP'])
    
    # Re-import data when region changes
    if region_previous != bird_game.region:
        bird_game.bird_image_df = load_image_data(bird_game.region)
        try:
            bird_game.bird_audio_df = load_audio_data(bird_game.region)
        except OSError:
            bird_game.bird_audio_df = pd.DataFrame(columns=['name','audio_id','cc'])

        bird_game.start_new_round()

    # Display game difficulty selection
    mode_previous = bird_game.mode
    bird_game.mode = st.sidebar.radio('Difficulty', ['1 :hatching_chick: beginner','2 :duck: intermediate','3 :eagle: advanced','4 :owl: twitcher'], 1)
    
    # If difficulty is changed, update the multichoice options
    if mode_previous != bird_game.mode:
        bird_game.start_new_round()
    
    # Display UI
    st.title('Twitch or Tweek')
    st.subheader('Name that bird!')  

    bird_game.display_ui()

    # Once a selection is made: update score, display animations, and start a new round
    if bird_game.selection is not None:
        bird_game.post_score_results(bird_game.selection)
        bird_game.start_new_round()
        bird_game.selection = None

    # Display Score
    if bird_game.guesses > 0:
        percentage = int(round(bird_game.score/bird_game.guesses,2)*100)
    else:
        percentage = 0

    st.sidebar.metric(label='Your Score:',value=f'{bird_game.score}/{bird_game.guesses}')
    st.sidebar.text(f'({percentage}%) {"🔥" if percentage>=90 else ""}')

# Import bird data
if 'bird_image_df' not in st.session_state:
    st.session_state.bird_image_df = pd.read_csv('data/images/au_images.csv')
    st.session_state.bird_audio_df = pd.read_csv('data/audio/au_audio.csv')

# Initialise game state
if 'bird_game' not in st.session_state:
    st.session_state.bird_game = BirdGame(st.session_state.bird_image_df, st.session_state.bird_audio_df)

# Play game
play_game(st.session_state.bird_game)
