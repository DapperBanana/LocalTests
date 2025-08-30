
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags

text = "This is a #sample text with #hashtags #PythonProgramming"
hashtags = extract_hashtags(text)

print("Hashtags found:")
for hashtag in hashtags:
    print(hashtag)
