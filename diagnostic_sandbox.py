
import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to perform sentiment analysis
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Get tweets and perform sentiment analysis
def get_tweets(query, count=10):
    tweets = api.search(q=query, count=count)
    for tweet in tweets:
        print(tweet.text)
        print("Sentiment: " + analyze_sentiment(tweet.text))
        print()

# Example usage
get_tweets("Python")

