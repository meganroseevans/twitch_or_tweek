import streamlit as st
import pandas as pd
import random
import requests

class BirdGame:
    def __init__(self, bird_images_df):
        self.bird_images_df = bird_images_df
        self.score = 0
        self.mode = 'hard mode'
        self.selection = None
        self.target_bird_name, self.target_bird_image, self.multichoice_options, self.correct_bird_index = self.new_game_state()
        self.buttons = [self.multichoice_options]

    def get_target_bird(self):
        selected_bird = self.bird_images_df.sample().iloc[0]
        return selected_bird['name'], selected_bird['image_id'], selected_bird['category']

    def get_multichoice_options(self, target_bird_name, target_bird_category):        
        if self.mode == 'easy mode':
            non_target_birds = [x for x in self.bird_images_df.name.unique().tolist() if x != target_bird_name]
        if self.mode == 'hard mode':
            non_target_birds = [x for x in self.bird_images_df[self.bird_images_df.category == target_bird_category].name.unique().tolist() if x != target_bird_name]

        # Determine the number of buttons to display and shuffle the order

        num_buttons = min(5, len(non_target_birds))
        multichoice_options = [target_bird_name] + random.sample(non_target_birds, num_buttons)
        random.shuffle(multichoice_options)

        correct_bird_index = multichoice_options.index(target_bird_name)

        return multichoice_options, correct_bird_index

    def new_game_state(self):
        self.target_bird_name, self.target_bird_image, target_bird_category = self.get_target_bird()
        self.multichoice_options, self.correct_bird_index = self.get_multichoice_options(self.target_bird_name, target_bird_category)

        return self.target_bird_name, self.target_bird_image, self.multichoice_options, self.correct_bird_index

    def post_score_results(self, selected_index):
        if self.correct_bird_index == selected_index:
            st.balloons()
            self.score += 1
        elif self.correct_bird_index != selected_index:
            st.snow()
            self.score -= 1

    def display_multichoice(self):
        for i, button_label in enumerate(self.multichoice_options):
            st.button(button_label, key=i, on_click=lambda i=i: self.register_selection(i))

    def register_selection(self, i):
        self.selection = i
    
    def deregister_selection(self):
        self.selection = None

    def display_ui(self):
        bird_image = f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{self.target_bird_image}/900'

        self.is_url_image(bird_image)

        # Layout with two columns
        image_column, buttons_column = st.columns([2, 1])

        with image_column:
            st.image(bird_image)

        with buttons_column:
            if self.selection is not None:
                st.write(f'This is a {self.target_bird_name}')
                st.button('Next', on_click=self.deregister_selection)

            else:
                self.display_multichoice()
        
    def is_url_image(self, image_url):
        r = requests.head(image_url)
        while r.status_code == 404:
           self.new_game_state()

def play_game(bird_game):
    
    st.title('Twitch or Tweek')

    mode_previous = bird_game.mode
    bird_game.mode = st.sidebar.radio('Difficulty', ['hard mode', 'easy mode'])
    
    if mode_previous != bird_game.mode:
        bird_game.new_game_state()

    st.subheader('Name that bird!')
    bird_game.display_ui()

    if bird_game.selection is not None:
        bird_game.post_score_results(bird_game.selection)
        bird_game.new_game_state()
        bird_game.selection = None

    st.sidebar.subheader("Your Score")
    st.sidebar.metric("score", bird_game.score, label_visibility='collapsed')

# app
if "bird_images_df" not in st.session_state:
    st.session_state.bird_images_df = pd.read_csv('data/ebird_images.csv')

if "bird_game" not in st.session_state:
    st.session_state.bird_game = BirdGame(st.session_state.bird_images_df)

play_game(st.session_state.bird_game)
