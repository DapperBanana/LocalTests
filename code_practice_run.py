
import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Perform sentiment analysis on Twitter data
def sentiment_analysis(query, count=10):
    tweets = api.search(q=query, count=count)

    for tweet in tweets:
        analysis = TextBlob(tweet.text)

        if analysis.sentiment.polarity > 0:
            sentiment = "Positive"
        elif analysis.sentiment.polarity == 0:
            sentiment = "Neutral"
        else:
            sentiment = "Negative"

        print(f"Tweet: {tweet.text}")
        print(f"Sentiment: {sentiment}")
        print()

# Perform sentiment analysis on a specific query
query = "Python programming"
sentiment_analysis(query, count=10)
