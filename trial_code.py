
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags

text = "Check out this #amazing Python program that extracts #hashtags from a given text #Python #programming"

hashtags = extract_hashtags(text)

print("Hashtags found in the text:")
for hashtag in hashtags:
    print(hashtag)
