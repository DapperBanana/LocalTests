
import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets
query = 'Your search query here'

public_tweets = api.search(query)

# Perform sentiment analysis on tweets
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    
    # Determine sentiment polarity
    if analysis.sentiment.polarity > 0:
        print(f'Tweet: {tweet.text}')
        print('Sentiment: Positive\n')
    elif analysis.sentiment.polarity < 0:
        print(f'Tweet: {tweet.text}')
        print('Sentiment: Negative\n')
    else:
        print(f'Tweet: {tweet.text}')
        print('Sentiment: Neutral\n')
