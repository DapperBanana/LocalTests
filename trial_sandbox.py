
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Create a SentimentIntensityAnalyzer object
sid = SentimentIntensityAnalyzer()

# Define a function to analyze sentiment in text
def analyze_sentiment(text):
    # Get the sentiment scores for the text
    sentiment_scores = sid.polarity_scores(text)
    
    # Determine the overall sentiment based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment

# Input text to analyze sentiment
text = "The movie was great and exciting. I loved every moment of it!"

# Analyze sentiment in the text
result = analyze_sentiment(text)

print(f"The sentiment in the text is: {result}")
