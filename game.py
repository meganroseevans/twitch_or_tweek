import streamlit as st
import random
import pandas as pd

def pick_new_birds(bird_images_df, mode):
    # Select a random bird entry from the DataFrame
    selected_bird = bird_images_df.sample().iloc[0]
    bird_name, bird_image, bird_category = selected_bird['name'], selected_bird['image_id'], selected_bird['category']

    # Determine other birds to display based on the game mode
    if mode == 'easy mode':
        other_birds = [x for x in bird_images_df.name.unique().tolist() if x != bird_name]
    elif mode == 'hard mode':
        other_birds = [x for x in bird_images_df[bird_images_df.category == bird_category].name.unique().tolist() if x != bird_name]

    # Determine the number of buttons to display and shuffle the order
    num_buttons = min(5, len(other_birds))
    birds_to_display = [bird_name] + random.sample(other_birds, num_buttons)
    random.shuffle(birds_to_display)

    # Determine the index of the correct bird in the shuffled list
    correct_bird_index = birds_to_display.index(bird_name)

    return bird_name, bird_image, birds_to_display, correct_bird_index

# app
st.title('Twitch or Tweek')
mode = st.sidebar.radio('Difficulty', ['hard mode', 'easy mode'])
st.subheader('Name that bird!')

if "bird_images" not in st.session_state:
    # Load bird images DataFrame if not in session state
    st.session_state.bird_images = pd.read_csv('data/ebird_images.csv')  # streamlit runs from the main directory rather than the subdirectory the python file is in
if "score" not in st.session_state:
    # Initialize the score in session state
    st.session_state.score = 0
if "selection_made" not in st.session_state:
    # Initialize the selection made flag in session state
    st.session_state.selection_made = False
if "current_bird" not in st.session_state:
    # Initialize current bird information in session state
    st.session_state.current_bird, st.session_state.current_bird_image, st.session_state.buttons, st.session_state.correct_bird_index = pick_new_birds(
        st.session_state.bird_images, mode
    )

# Layout with two columns
col_image, col_buttons_1 = st.columns([2, 1])

with col_image:
    # Display bird image
    st.image(f'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{st.session_state.current_bird_image}/1200')

    if not st.session_state.selection_made:
        with col_buttons_1:
            # Display buttons for bird names
            for i in range(len(st.session_state.buttons)):
                button_label = st.session_state.buttons[i]
                buttons = st.button(button_label)

                # Check if correct bird button is pressed
                if buttons and st.session_state.correct_bird_index == i:
                    st.balloons()  # Celebrate correct answer
                    st.session_state.score += 1
                    st.session_state.selection_made = True
                elif buttons and st.session_state.correct_bird_index != i:
                    st.snow()  # Indicate incorrect answer
                    st.session_state.score -= 1
                    st.session_state.selection_made = True

if st.session_state.selection_made:
    # Display correct bird name after selection is made
    st.write(f'This is a {st.session_state.current_bird}')
    next_button = st.button('Next')
    # Load new bird information for the next round
    st.session_state.current_bird, st.session_state.current_bird_image, st.session_state.buttons, st.session_state.correct_bird_index = pick_new_birds(
        st.session_state.bird_images, mode
    )
    st.session_state.selection_made = False

# Display score in the sidebar
st.sidebar.subheader("Your Score")
st.sidebar.metric("score", st.session_state.score, label_visibility='collapsed')
