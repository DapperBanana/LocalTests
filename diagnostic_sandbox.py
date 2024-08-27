
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    # Print the sentiment polarity
    if analysis.sentiment.polarity > 0:
        print("Positive sentiment")
    elif analysis.sentiment.polarity < 0:
        print("Negative sentiment")
    else:
        print("Neutral sentiment")

# Input text
text = input("Enter text to analyze sentiment: ")

# Analyze sentiment
analyze_sentiment(text)
