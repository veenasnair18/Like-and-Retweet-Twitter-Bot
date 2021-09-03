# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 13:53:46 2021

@author: Veena
"""
import tweepy
import time


auth = tweepy.OAuthHandler('IxigNQwF5aSPD3UTBfiFbr45G','ozOJABMrkPER9sBjzm32YCarDjsD9NTXK5b4CABWUUPzVqsBN9')

auth.set_access_token('1312624262797123584-GBr3u0DRMBwHabZJcEtGCg1LowSiKe','S5YgdqbCzNBqKC6M5QCGNf3s0v9mHDHIKIz1J5WwfPLDF')

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user = api.me()

search = "Python"

notweets=10

for tweet in tweepy.Cursor(api.search,search).items(notweets):
    try:
        print("Liked Tweets!")
        tweet.retweet()
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
    
    
    

