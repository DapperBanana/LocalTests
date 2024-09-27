
from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment score
    sentiment_score = blob.sentiment.polarity
    
    # Determine sentiment based on score
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment

# Get input text from user
text = input("Enter some text to analyze sentiment: ")

# Analyze sentiment
sentiment = analyze_sentiment(text)

print(f"Sentiment: {sentiment}")
