import datetime
import os

import tweepy


def auth():
    auth = tweepy.OAuthHandler(
        os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"]
    )
    auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

    return auth


def gen_text() -> str:
    text = "{}月{}日の天気は{}です。".format(
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        "晴れ",
    )

    return text


def tweet(img_path: str):
    api: tweepy.OAuthHandler = tweepy.API(auth())
    text: str = gen_text()

    api.update_with_media(img_path, text)
