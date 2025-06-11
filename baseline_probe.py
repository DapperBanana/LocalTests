
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    # Check for sentiment polarity
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Input text to analyze sentiment
text = "I love Natural Language Processing!"
sentiment = analyze_sentiment(text)

print(f"The sentiment of the text is: {sentiment}")
