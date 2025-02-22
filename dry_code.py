
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Load the sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

# Input text to analyze sentiment
text = "I love spending time with my friends, they always make me happy."

# Analyze the sentiment of the text
sentiment_scores = sid.polarity_scores(text)

# Determine the sentiment from the scores
if sentiment_scores['compound'] >= 0.05:
    sentiment = "Positive"
elif sentiment_scores['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Print the sentiment of the text
print("Sentiment of the text: " + sentiment)
