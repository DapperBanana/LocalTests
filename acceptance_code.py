
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Create a SentimentIntensityAnalyzer object
sid = SentimentIntensityAnalyzer()

# Get input text from user
text = input("Enter text to analyze sentiment: ")

# Analyze sentiment of the text
scores = sid.polarity_scores(text)

# Determine sentiment based on compound score
if scores['compound'] >= 0.05:
    print("Positive sentiment")
elif scores['compound'] <= -0.05:
    print("Negative sentiment")
else:
    print("Neutral sentiment")

# Print the sentiment scores
print("\nSentiment Scores:")
for score in scores:
    print(f"{score}: {scores[score]}")
