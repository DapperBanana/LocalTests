
import tweepy
from textblob import TextBlob

# Authenticate to Twitter
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Get tweets
tweets = api.search(q='Python', count=10)

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    
    # Perform sentiment analysis
    if analysis.sentiment.polarity > 0:
        print('Sentiment: Positive')
    elif analysis.sentiment.polarity == 0:
        print('Sentiment: Neutral')
    else:
        print('Sentiment: Negative')
    print('\n')
