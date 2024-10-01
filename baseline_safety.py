
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    # Initialize the VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    
    # Get the sentiment scores for the text
    sentiment_scores = sid.polarity_scores(text)
    
    # Determine the overall sentiment based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        return "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Example text to analyze
text = "I love this movie! It's so amazing and inspiring."

# Analyze the sentiment of the text
sentiment = analyze_sentiment(text)
print(f"The sentiment of the text is: {sentiment}")
