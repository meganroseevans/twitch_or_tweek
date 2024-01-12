import streamlit as st
import random
import pandas as pd

def pick_new_birds(bird_images_df, mode):
    selected_bird = bird_images_df.sample()
    bird_name, bird_image, bird_category = selected_bird.iloc[0,0], selected_bird.iloc[0,1], selected_bird.iloc[0,2]
    birds_in_category = bird_images_df[bird_images_df.category==bird_category].name.unique().tolist()
    all_other_birds = bird_images_df.name.unique().tolist()
    if mode == 'easy mode':
        other_birds = [x for x in all_other_birds if x != bird_name]
    elif mode == 'hard mode':
        other_birds = [x for x in birds_in_category if x != bird_name]
    num_buttons = min(5,len(other_birds))
    birds_to_display = [bird_name] + random.sample(other_birds,num_buttons)
    random.shuffle(birds_to_display)
    correct_bird_index = birds_to_display.index(bird_name)
    return bird_name, bird_image, birds_to_display, correct_bird_index

# app
st.title('Twitch or Tweek')
mode = st.sidebar.radio('Difficulty',['hard mode','easy mode'])
st.subheader('Name that bird!')

if "bird_images" not in st.session_state:
    st.session_state.bird_images = pd.read_csv('ebird_images.csv') #streamlit runs from the main directory rather than the subdirectory the python file is in
if "score" not in st.session_state:
    st.session_state.score = 0
if "time_to_guess" not in st.session_state:
    st.session_state.time_to_guess = True
if "time_to_refresh" not in st.session_state:
    st.session_state.time_to_refresh = False
if "selection_made" not in st.session_state:
    st.session_state.selection_made = False
if "current_bird" not in st.session_state:
    st.session_state.current_bird, st.session_state.current_bird_image, st.session_state.buttons, st.session_state.correct_bird_index = pick_new_birds(st.session_state.bird_images, mode)

# st.components.v1.html(f"""
#                       <iframe src="https://macaulaylibrary.org/asset/496551851/embed" height="383" width="640" frameborder="0" allowfullscreen></iframe>
#                       """)

col_image, col_buttons_1 = st.columns([2,1])

with col_image:
    st.image(f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{st.session_state.current_bird_image}/1200')
    # for audio clips

with col_buttons_1:
    if not st.session_state.selection_made:
        for i in range(len(st.session_state.buttons)):
            buttons = st.button(f'{st.session_state.buttons[i]}')
            if buttons and st.session_state.correct_bird_index == i:
                st.balloons()
                st.session_state.score +=1
                st.session_state.selection_made = True
            elif buttons and st.session_state.correct_bird_index != i:
                st.snow()
                st.session_state.score -=1
                st.session_state.selection_made = True
    if st.session_state.selection_made:
        st.session_state.current_bird, st.session_state.current_bird_image, st.session_state.buttons, st.session_state.correct_bird_index = pick_new_birds(st.session_state.bird_images ,mode)
        st.session_state.selection_made = False
        
st.sidebar.subheader("Your Score")
st.sidebar.metric("score",st.session_state.score,label_visibility='collapsed')

