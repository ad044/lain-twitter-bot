from os import path, getcwd, listdir
import random
import tweepy


auth = tweepy.OAuthHandler("",
                           "")
auth.set_access_token("",
                      "")

ANIME_SUBS_DIR = "anime_subtitles/picked_subtitle_data"
GAME_SUBS_DIR = "game_subtitles/picked_subtitle_data"

anime_quotes = []
game_quotes = []

for filename in listdir(path.join(getcwd(), ANIME_SUBS_DIR)):
    with open(path.join(getcwd(), ANIME_SUBS_DIR, filename), 'r') as f:
        for line in f.read().splitlines():
            if line.strip():
                anime_quotes.append(line)

with open(path.join(getcwd(), GAME_SUBS_DIR, "subs.txt"), "r") as f:
    for line in f.read().splitlines():
        if line.strip():
            game_quotes.append(line)


final_quote_list = anime_quotes + game_quotes

api = tweepy.API(auth)

public_tweets = api.home_timeline(200)

while True:
    chosen_quote = random.choice(final_quote_list)
    if chosen_quote not in public_tweets:
        api.update_status(chosen_quote)
        break