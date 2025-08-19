
import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = "<YOUR_CONSUMER_KEY>"
consumer_secret = "<YOUR_CONSUMER_SECRET>"
access_token = "<YOUR_ACCESS_TOKEN>"
access_token_secret = "<YOUR_ACCESS_TOKEN_SECRET>"

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets containing a specific keyword
keyword = "Python"
public_tweets = api.search(q=keyword, count=10)

# Perform sentiment analysis on each tweet
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    print("Tweet: ", tweet.text)
    print("Sentiment: ", analysis.sentiment)
    print()

