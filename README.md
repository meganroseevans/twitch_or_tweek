# My Bird Game

Head to https://twitch-or-tweek.streamlit.app/ to play 🎉

<video width="400" height="240" controls>
  <source src="assets/twitch_or_tweek_clip.mov" type="video/mp4">
</video>

## To run locally

Prerequisites, you'll need docker installed. Either head to [this link](https://docs.docker.com/get-docker/) or if you have home brew run:
```zsh
brew install docker
```

To play, run:
```zsh
$ auto/twitch
```

## The Game

Twitch or Tweek is a bird naming game to help me (and fellow twitchers) practise their bird identification. Guess the bird shown in the image.

There are four modes which change the options presented in the multi-choice buttons:
- `🥚 beginner`: Three (3) multi-choice options randomly selected from ALL birds in Australia
- `🐣 intermediate`: Four (4) multi-choice options randomly selected from ALL birds in Australia
- `🦆 advanced`: Five (5) multi-choice options randomly selected from similar birds to the one shown in the image
- `🦅 twitcher`: Six (6) multi-choice options randomly selected from similar birds to the one shown in the image

## To Do

- [x] Dockerize (see [Dockerfile](./Dockerfile), [docker-compose.yaml](./docker-compose.yaml) and [auto/twitch](./auto/twitch))
- [x] Fix bug: Double click to reload
- [x] Fix bug: Instant easy-hard mode switch (post-mortem: streamlit `on_click` function runs prior to variable assigment, fix: check for mode change)
- [x] Find way to collect bird data without click ops (see [get_bird_images.js](./data/get_bird_images.js))
- [ ] Audio clips
- [ ] Better categorisation, e.g. grouping by bird colours and genus
- [ ] Make bird data script automated with Lambda & S3
- [ ] Work out a way to do a Delta of new and existing data
- [ ] Consider doing enrichment within S3
- [ ] Look into JSON rather than CSV - wider use format, faster to read(?)
- [ ] Try to run bird grouping SQL locally
- [ ] Add tests - 1) UI app so build tests to check user interactions 2) Test backend for things exposed to user or shared internally

## Data Sources

- eBird’s API - [https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest](https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest#36c95b76-e18e-4788-9c9e-e539045f9166)
- Cornell Lab of Ornithology - https://ebird.org/home
- Cornell’s Bird Academy - [https://academy.allaboutbirds.org](https://academy.allaboutbirds.org/)
