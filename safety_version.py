
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Input text to analyze
text = "I love this product, it works really well. However, the customer service was terrible."

# Get the sentiment score of the text
sentiment_score = sid.polarity_scores(text)

# Determine the overall sentiment
if sentiment_score['compound'] >= 0.05:
    sentiment = "Positive"
elif sentiment_score['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Print the sentiment analysis results
print("Sentiment Analysis Results:")
print("-----------------------------")
print("Text: ", text)
print("Overall sentiment: ", sentiment)
print("Sentiment score: ", sentiment_score)
