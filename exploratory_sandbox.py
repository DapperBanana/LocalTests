
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

text = "I love this movie, it's amazing!"
sentiment = analyze_sentiment(text)

print(f"The sentiment of the text is: {sentiment}")
