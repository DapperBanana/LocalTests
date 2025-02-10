
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
    

def main():
    text = input("Enter the text to analyze sentiment: ")
    sentiment = analyze_sentiment(text)
    
    print("Sentiment of the text is:", sentiment)

if __name__ == "__main__":
    main()
