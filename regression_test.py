
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

if __name__ == "__main__":
    text = "I love this movie, it was so good!"
    sentiment = analyze_sentiment(text)
    print(f"The sentiment of the text is: {sentiment}")
