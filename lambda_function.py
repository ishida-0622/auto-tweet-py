import requests
import tweepy
import os
import sys
sys.path.append("python")


def lambda_handler(event, context):
    url = "https://weather.tsukumijima.net/api/forecast/city/130010"
    request = requests.get(url)
    result = request.json()
    TEXT = (
        str(result["forecasts"][0]["date"]).replace("-", "/") + " の "
        + result["title"] + "\n"
        + str(result["forecasts"][0]["detail"]["weather"]).replace("　", " ") + "\n"
        + "最低気温は" + str(result["forecasts"][0]["temperature"]["min"]["celsius"]) + "度" + " "
        + "最高気温は" + str(result["forecasts"][0]["temperature"]["max"]["celsius"]) + "度です" + "\n\n"
        + result["copyright"]["title"] + "\n"
        + result["copyright"]["link"]
    )

    api_key = os.environ["API_KEY"]
    api_key_secret = os.environ["API_KEY_SECRET"]
    access_token = os.environ["ACCESS_TOKEN"]
    access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(TEXT)
