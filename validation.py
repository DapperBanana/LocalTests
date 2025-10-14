
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    # Check if sentiment is positive, negative, or neutral
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Input the text to be analyzed
text = input("Enter the text to be analyzed: ")

sentiment = analyze_sentiment(text)
print("Sentiment analysis result:", sentiment)
