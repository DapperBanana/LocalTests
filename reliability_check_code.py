
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    
    sentiment_score = blob.sentiment.polarity
    
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

text = "I love this product! It works really well."
sentiment = analyze_sentiment(text)

print("Sentiment analysis result:", sentiment)
