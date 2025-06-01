
import tweepy
from textblob import TextBlob

# Set up Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get tweets from a specific user
screen_name = 'realDonaldTrump'
tweets = api.user_timeline(screen_name, count=10)

# Perform sentiment analysis on each tweet
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        print(f'"{tweet.text}" - Positive sentiment')
    elif analysis.sentiment.polarity < 0:
        print(f'"{tweet.text}" - Negative sentiment')
    else:
        print(f'"{tweet.text}" - Neutral sentiment')
