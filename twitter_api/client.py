import tweepy
from twitter_api.keys import *


class TwitterClient:

    def __init__(self, username):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth, proxy='http://127.0.0.1:8123')
        self.user = self.api.get_user(username)

    def get_user_tweet_texts(self, count=100):
        return [tweet.text for tweet in self.api.user_timeline(count=count)]
