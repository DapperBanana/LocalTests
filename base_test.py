
import re

def extract_hashtags(text):
    hashtags = re.findall(r'\#\w+', text)
    return hashtags

text = "I love #python and #coding! #programming is fun."
hashtags = extract_hashtags(text)

for hashtag in hashtags:
    print(hashtag)
