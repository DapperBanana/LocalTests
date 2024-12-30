
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

# Input text for sentiment analysis
text = "I love this movie. It's so amazing!"

# Analyze sentiment in the text
sentiment_score = sia.polarity_scores(text)

# Print the sentiment score
print(sentiment_score)
