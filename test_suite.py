
from textblob import TextBlob

# Define some sample text
text = "I love this movie! It's so good and funny."

# Create a TextBlob object
blob = TextBlob(text)

# Calculate sentiment polarity
sentiment = blob.sentiment.polarity

# Determine sentiment based on polarity
if sentiment > 0:
    print("Positive sentiment")
elif sentiment < 0:
    print("Negative sentiment")
else:
    print("Neutral sentiment")
