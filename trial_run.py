
import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get user input for Twitter username
username = input("Enter Twitter username to perform sentiment analysis on: ")

# Get tweets from specified user
tweets = api.user_timeline(screen_name=username, count=10)

# Perform sentiment analysis on each tweet
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    
    # Print tweet and sentiment analysis result
    print(f"Tweet: {tweet.text}")
    print(f"Sentiment: {'Positive' if analysis.sentiment.polarity > 0 else 'Negative' if analysis.sentiment.polarity < 0 else 'Neutral'}\n")
