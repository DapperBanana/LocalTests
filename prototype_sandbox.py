
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

text = "Hello world! #Python is awesome. #coding #programming"

hashtags = extract_hashtags(text)

for hashtag in hashtags:
    print(hashtag)
