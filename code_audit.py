
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon if needed
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    # Create an instance of the SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Get the sentiment scores for the text
    sentiment_scores = analyzer.polarity_scores(text)
    
    # Interpret the sentiment scores
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment

# Example usage
text = "I love this movie! It's amazing."
sentiment = analyze_sentiment(text)
print(sentiment)
