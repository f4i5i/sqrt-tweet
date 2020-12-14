import requests
import os
import json
import tweepy as tw
from .models import *

def tweet_call():
    consumer_key= 'LPRNQ1tnxqIuphhHsfoIF7y4g'
    consumer_secret= 'jioxDFvacJTpwjhnojNTQPoxGs6R2z44Ez5pgIjdznFW7HrCkb'
    access_token= '1087910265323249664-46zWMEL1T2yNOjuwVnos5WXi0VMnev'
    access_token_secret= 'g6wAeMUOj2rrz4wPR4Ce02FYAavE0BDYEQEoyTtritkxZ'
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    search_words = "#Covid"
    date_since = "2018-11-16"

    tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items(100)
    for tweet in tweets:
        twt_id = tweet.id
        twt_time = tweet.created_at
        twt_txt = tweet.text
        obj , created = Tweets.objects.get_or_create(tweet_id = str(twt_id), tweet_time = str(twt_time), tweet_text= str(twt_txt))