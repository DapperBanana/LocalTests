letion(id='chatcmpl-9TxlXV2hyWjWkfJv6NlOQTNUAGxdl', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# download Vader lexicon
nltk.download('vader_lexicon')

# create SentimentIntensityAnalyzer object
sid = SentimentIntensityAnalyzer()

# define function to analyze sentiment in text
def analyze_sentiment(text):
    # get sentiment scores
    scores = sid.polarity_scores(text)
    
    # determine sentiment label based on compound score
    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# input text to analyze sentiment
text = "I love going to the beach on a sunny day."
sentiment = analyze_sentiment(text)

print("Sentiment of the text: ", sentiment)', role='assistant', function_call=None, tool_calls=None))], created=1716928279, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=168, prompt_tokens=23, total_tokens=191)