
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

# Perform sentiment analysis on tweets
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Get tweets from a specific user
tweets = api.user_timeline(screen_name='realDonaldTrump', count=10)

# Analyze the sentiment of each tweet and print the results
for tweet in tweets:
    print(tweet.text)
    print("Sentiment: " + analyze_sentiment(tweet.text))
    print()

