import datetime
import os

import tweepy


class Twitter:
    def __init__(self):
        self.token: tweepy = None
        self.text: tweepy = None

    def auth(self) -> None:
        self.token.set_access_token(os.environ["AT"], os.environ["AS"])
        self.token = tweepy.OAuthHandler(os.environ["CK"], os.environ["CS"])
        self.api: tweepy = tweepy.API(self.token)

    def gen_text(self) -> None:
        self.text = "{}月{}日の天気は{}です。".format(
            datetime.datetime.now().month,
            datetime.datetime.now().day,
            "晴れ",
        )

    def tweet(self, img_path: str) -> None:
        self.api.update_with_media(img_path, self.text)
