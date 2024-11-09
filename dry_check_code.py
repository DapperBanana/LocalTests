
import re

def extract_hashtags(text):
    hashtags = re.findall(r'\B#\w+', text)
    return hashtags

text = "Check out this amazing #python program that extracts all #hashtags from a given text #programming #coding"
hashtags = extract_hashtags(text)

print("Hashtags found in the text:")
for hashtag in hashtags:
    print(hashtag)
