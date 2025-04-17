
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Create a SentimentIntensityAnalyzer object
sid = SentimentIntensityAnalyzer()

# Define the text for analysis
text = "I love this movie! It's so exciting and well-made."

# Analyze the sentiment of the text
sentiment_scores = sid.polarity_scores(text)

# Print the sentiment scores
print("Sentiment scores:")
for key, value in sentiment_scores.items():
    print(f"{key}: {value}")

# Determine the overall sentiment
if sentiment_scores['compound'] >= 0.05:
    print("Overall sentiment: Positive")
elif sentiment_scores['compound'] <= -0.05:
    print("Overall sentiment: Negative")
else:
    print("Overall sentiment: Neutral")
