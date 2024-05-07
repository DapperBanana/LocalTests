
import tweepy
from textblob import TextBlob

# Insert your Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate Tweepy with your API credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get tweets containing a specific keyword
search_query = "python"
public_tweets = api.search(q=search_query, count=100)

# Perform sentiment analysis on each tweet
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        print(f"Positive: {tweet.text}")
    elif polarity < 0:
        print(f"Negative: {tweet.text}")
    else:
        print(f"Neutral: {tweet.text}")
