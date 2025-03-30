
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

text = "I love #coding and #programming in #Python"
hashtags = extract_hashtags(text)

print("Hashtags found in the text:")
for hashtag in hashtags:
    print(hashtag)
