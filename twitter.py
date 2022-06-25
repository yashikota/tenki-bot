import datetime
import json
import os

import requests
import tweepy


class Twitter:
    def __init__(self):
        self.token: tweepy = None
        self.api: tweepy = None
        self.text: tweepy = None
        self.weather: str = ""

    def auth(self) -> None:
        self.token.set_access_token(os.environ["AT"], os.environ["AS"])
        self.token = tweepy.OAuthHandler(os.environ["CK"], os.environ["CS"])
        self.api = tweepy.API(self.token)

    def get_weather(self) -> None:
        url: str = "https://www.jma.go.jp/bosai/forecast/data/forecast/270000.json"
        res: str = requests.get(url).text
        data: list = json.loads(res)
        timeseries: list = data[0]["timeseries"]
        areas: list = timeseries[0]["areas"]
        self.weather = areas[0]["weathers"][0]

    def gen_text(self) -> None:
        self.text = "{}月{}日の天気は{}です。".format(
            datetime.datetime.now().month,
            datetime.datetime.now().day,
            self.weather,
        )

    def tweet(self, img_path: str) -> None:
        self.api.update_with_media(img_path, self.text)
