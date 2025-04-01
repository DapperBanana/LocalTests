
import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to perform sentiment analysis on a tweet
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Search for tweets with a specific keyword
keyword = "Python"
tweets = api.search(q=keyword, count=10)

# Perform sentiment analysis on each tweet and print the result
for tweet in tweets:
    print(f"Tweet: {tweet.text}")
    sentiment = analyze_sentiment(tweet.text)
    print(f"Sentiment: {sentiment}\n")
