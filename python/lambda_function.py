import tweepy
import requests

url = "https://weather.tsukumijima.net/api/forecast/city/130010"
request = requests.get(url)
result = request.json()
# TEXT = (
#   str(result["forecasts"][0]["date"]).replace("-", "/") + " の "
#   + result["title"] + "\n"
#   + str(result["forecasts"][0]["detail"]["weather"]).replace("　"," ") + "\n"
#   + "最低気温は" + str(result["forecasts"][0]["temperature"]["min"]["celsius"]) + "度" + " "
#   + "最高気温は" + str(result["forecasts"][0]["temperature"]["max"]["celsius"]) + "度です" + "\n\n"
#   + result["copyright"]["title"] + "\n"
#   + result["copyright"]["link"]
# )
TEXT = "twitter for AWS Lambda"

k = "2nHZfekb9tRu3vfKGZh7blcJ4"
ks = "iPygo9q5103bipiMEJeFlHTTAP3rkU33dwQdfhe0WG4GFOfoeg"
t = "1529018614321643521-NssvmKmxcnMK6IVuxURnaPz7UfXJf6"
ts = "dapiPQaivMyy8sWhT4hd7KaydTnpoTMpRc5cDRuysfUcx"
auth = tweepy.OAuthHandler(k, ks)
auth.set_access_token(t, ts)
api = tweepy.API(auth)
api.update_status(TEXT)
