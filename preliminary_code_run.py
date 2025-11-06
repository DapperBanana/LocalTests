
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

text = "Here are some #hashtags to extract from this text: #Python #programming #hashtag"
hashtags = extract_hashtags(text)

for hashtag in hashtags:
    print(hashtag)
