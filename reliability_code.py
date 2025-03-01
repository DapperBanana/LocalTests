
import tweepy
from textblob import TextBlob

# Authenticate with Twitter API
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Get tweets from a specific user
username = 'realDonaldTrump'
tweets = api.user_timeline(screen_name=username, count=10)

# Perform sentiment analysis on each tweet
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    print(tweet.text)
    print('Sentiment:', analysis.sentiment)
    print()

