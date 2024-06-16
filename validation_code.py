
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

# Function to perform sentiment analysis
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity

# Fetch tweets based on keyword
def fetch_tweets(keyword, count=10):
    tweets = api.search(q=keyword, count=count)
    return tweets

# Perform sentiment analysis on fetched tweets
def perform_sentiment_analysis(keyword, count=10):
    tweets = fetch_tweets(keyword, count)
    for tweet in tweets:
        print(tweet.text)
        sentiment_score = analyze_sentiment(tweet.text)
        if sentiment_score > 0:
            print('Sentiment: Positive')
        elif sentiment_score < 0:
            print('Sentiment: Negative')
        else:
            print('Sentiment: Neutral')
        print()

# Run sentiment analysis on Twitter data
keyword = 'Python'
perform_sentiment_analysis(keyword, count=10)
