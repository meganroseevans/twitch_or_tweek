# My Bird Game

In Oct 2022, I created a basic bird identification game using Streamlit. There’s a few changes I’d like to make to it, including: deploying as a real website, ironing out glitches and bugs, convert it from streamlit to a pure python program.

<video width="400" height="240" controls>
  <source src="twitch_or_tweek_clip.mov" type="video/mp4">
</video>

## Set Up

Prerequisites, install streamlit by running:
```zsh
pip3 install streamlit
```

To play, run:
```zsh
streamlit run game.py
```

## The Game

Twitch or Tweek is a bird naming game to help me (and fellow twitchers) practise their bird identification. Guess the bird shown in the image.

There are two modes which change the options presented in the multi-choice buttons:
- `easy`: Multi-choice is made up of a random selection of ALL birds in Australia
- `hard`: Multi-choice is made up of ONLY similar birds to the one shown in the image

## To Do

1. Dockerize
1. Fix bug: double click to reload
1. Instant easy-hard mode switch
1. Connect to a continuous data source, e.g. a bird image API if one exists

## Data Sources

- eBird’s API - [https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest](https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest#36c95b76-e18e-4788-9c9e-e539045f9166)
- Cornell Lab of Ornithology - https://ebird.org/home
- Cornell’s Bird Academy - [https://academy.allaboutbirds.org](https://academy.allaboutbirds.org/)
