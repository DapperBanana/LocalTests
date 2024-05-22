
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Get input text from user
text = input("Enter the text you want to analyze: ")

# Analyze sentiment
sentiment = analyze_sentiment(text)

print("Sentiment of the text is:", sentiment)
