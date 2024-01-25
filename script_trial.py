
from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object with the given text
    blob = TextBlob(text)
    
    # Use the sentiment property of the TextBlob object to get sentiment values
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Determine the sentiment label based on polarity value
    if polarity > 0:
        sentiment_label = "Positive"
    elif polarity < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    # Print the sentiment information
    print("Text: ", text)
    print("Sentiment: ", sentiment_label)
    print("Polarity: ", polarity)
    print("Subjectivity: ", subjectivity)

# Example usage
text = "I love this product! It's fantastic."
analyze_sentiment(text)
