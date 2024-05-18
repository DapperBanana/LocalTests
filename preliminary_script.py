
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)
    
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == "__main__":
    text = input("Enter the text to analyze sentiment: ")
    
    sentiment = get_sentiment(text)
    print(f"The sentiment of the text is: {sentiment}")
