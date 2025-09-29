
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

# Search for tweets
search_query = 'Python'
public_tweets = api.search(q=search_query, lang='en', count=100)

# Perform sentiment analysis on each tweet
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        print(f'Tweet: {tweet.text}')
        print('Sentiment: Positive')
    elif analysis.sentiment.polarity < 0:
        print(f'Tweet: {tweet.text}')
        print('Sentiment: Negative')
    else:
        print(f'Tweet: {tweet.text}')
        print('Sentiment: Neutral')
