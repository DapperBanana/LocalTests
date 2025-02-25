
from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity
    
    # Classify the sentiment as positive, negative, or neutral based on polarity
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return sentiment, polarity

if __name__ == '__main__':
    # Input text to analyze
    text = input("Enter text to analyze sentiment: ")
    
    # Analyze sentiment in the text
    sentiment, polarity = analyze_sentiment(text)
    
    print(f"Sentiment: {sentiment}")
    print(f"Sentiment Polarity: {polarity}")
