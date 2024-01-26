import streamlit as st
import pandas as pd
import random
import requests

class BirdGame:
    def __init__(self, bird_images_df):
        """Initialise game state"""
        self.bird_images_df = bird_images_df
        self.score = 0
        self.region = 'AU'
        self.mode = ' intermediate'
        self.selection = None
        self.target_bird_name, self.target_bird_image, self.multichoice_options, self.correct_bird_index = self.start_new_round()
        self.buttons = [self.multichoice_options]

    def get_target_bird(self):
        """Select a bird at random"""
        selected_bird = self.bird_images_df.sample().iloc[0]
        return selected_bird['name'], selected_bird['image_id'], selected_bird['category']

    def get_multichoice_options(self, target_bird_category):
        """Return list of bird names for multichoice button labels, based on game difficulty."""

        # Set multichoice options based on game difficulty
        if self.mode == ':hatching_chick: beginner':
            num_options = 2
            non_target_birds = [x for x in self.bird_images_df.name.unique().tolist() if self.target_bird_name not in x]            
        elif self.mode == ':eagle: advanced':
            num_options = 4
            non_target_birds = [x for x in self.bird_images_df[self.bird_images_df.category == target_bird_category].name.unique().tolist() if x != self.target_bird_name]
        elif self.mode == ':owl: twitcher':
            num_options = 5
            non_target_birds = [x for x in self.bird_images_df[self.bird_images_df.category == target_bird_category].name.unique().tolist() if x != self.target_bird_name]
        else:
            num_options = 3
            non_target_birds = [x for x in self.bird_images_df.name.unique().tolist() if self.target_bird_name not in x]

        # Select random sample of bird names for button labels
        multichoice_options = [self.target_bird_name] + random.sample(non_target_birds, min(num_options, len(non_target_birds)))
        random.shuffle(multichoice_options)

        # Register button index containing target bird
        correct_bird_index = multichoice_options.index(self.target_bird_name)

        if len(non_target_birds) < num_options - 1:
            self.start_new_round()
            st.write(non_target_birds)

        return multichoice_options, correct_bird_index

    def start_new_round(self):
        """Select a new bird and multichoice options. Reset 'selection' to None.
        
        returns:
            - target_bird_name (str): name of bird to display
            - target_bird_image (str): ID of image to display
            - multichoice_options (list): multichoice button labels of bird names
            - correct_bird_index (int): index in multichoice list of target bird 
        """
        self.target_bird_name, self.target_bird_image, self.target_bird_category = self.get_target_bird()
        self.multichoice_options, self.correct_bird_index = self.get_multichoice_options(self.target_bird_category)

        return self.target_bird_name, self.target_bird_image, self.multichoice_options, self.correct_bird_index

    def post_score_results(self, selected_index):
        """Update score and play animations based on user's answer"""
        if self.correct_bird_index == selected_index:
            st.balloons()
            self.score += 1
        elif self.correct_bird_index != selected_index:
            st.snow()
            self.score -= 1

    def display_multichoice(self):
        """Create multichoice buttons to display in right column"""
        for i, button_label in enumerate(self.multichoice_options):
            st.button(button_label, key=i, on_click=lambda i=i: self.register_selection(i))

    def register_selection(self, i):
        self.selection = i
    
    def deregister_selection(self):
        self.selection = None

    def display_ui(self):
        """Display the game interface: images, buttons, text."""
        # Create two columns for side-by-side image and buttons
        image_column, buttons_column = st.columns([2, 1])

        # Display image
        with image_column:
            bird_image = f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{self.target_bird_image}/900'
            self.check_image_health(bird_image)
            st.image(bird_image)

        # Pre-selection show multichoice buttons. Post-selection show bird name and 'Next'.
        with buttons_column:
            if self.selection is not None:
                st.write(f'This is a {self.target_bird_name}')
                st.button('Next', on_click=self.deregister_selection)
            else:
                self.display_multichoice()
        
    def check_image_health(self, image_url):
        """Skip unhealthy/missing images by triggering a new round"""
        r = requests.head(image_url)
        while r.status_code == 404:
           self.start_new_round()

def play_game(bird_game):
    """Play Twitch or Tweek"""

    # Display region select
    region_previous = bird_game.region
    bird_game.region = st.sidebar.selectbox('Region:',options=['AU','GB','JP','LK'])
    
    # Re-import data when region changes
    if region_previous != bird_game.region:
        bird_game.bird_images_df = pd.read_csv(f'data/regional/{bird_game.region.lower()}_images.csv')
        bird_game.start_new_round()

    # Display game difficulty selection
    mode_previous = bird_game.mode
    bird_game.mode = st.sidebar.radio('Difficulty', [':hatching_chick: beginner',':duck: intermediate',':eagle: advanced',':owl: twitcher'], 1)
    
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
    st.sidebar.subheader("Your Score")
    st.sidebar.metric("score", bird_game.score, label_visibility='collapsed')

# Import image data
if "bird_images_df" not in st.session_state:
    st.session_state.bird_images_df = pd.read_csv('data/regional/au_images.csv')

# Initialise game state
if "bird_game" not in st.session_state:
    st.session_state.bird_game = BirdGame(st.session_state.bird_images_df)

# Play game
play_game(st.session_state.bird_game)
