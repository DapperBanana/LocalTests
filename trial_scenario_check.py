
import tweepy
from textblob import TextBlob

# Step 1: Authenticate with Twitter API
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 2: Get tweets from timeline
public_tweets = api.home_timeline()

# Step 3: Perform sentiment analysis on each tweet
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    
    # Step 4: Print tweet and sentiment
    print(f'Tweet: {tweet.text}')
    print(f'Sentiment: {analysis.sentiment}\n')
