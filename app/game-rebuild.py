import random
import pandas as pd

# presets

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

# presets

data_df = pd.read_csv('data/ebird_images.csv')
names_df = data_df[["name","category"]].drop_duplicates()

score = 0
# current_bird, current_bird_image = pick_new_birds(bird_images, mode)

# app
print("Welcome to 'Twitch or Tweek'")
print('Name that bird!')

print("Choose your difficulty: hard mode [h] or easy mode [e]]")
mode = input("> ")

target = data_df.sample()

if mode == 'e':
    non_target = names_df[names_df.name.values != target.name.values].sample(4)
elif mode == 'h':
    non_target = names_df.loc[(names_df.category.values == target.category.values) & (names_df.name.values != target.name.values)].sample(4)

# non_target = names_df[
#     ((mode == 'h') & names_df.category.eq(target.category.values[0])) &
#     (~names_df.name.isin(target.name.values))
# ].sample(4)

print('target')
print(target)
print('non_target')
print(non_target)

#print(f"This bird is a {target.name.to_string(index=False)}")
#print(f"Some other birds are {non_target.name.to_string(index=False)}")

#bird_image
#print(f"https://cdn.download.ams.birds.cornell.edu/api/v1/asset/{bird_images.image[0]}/1200")
