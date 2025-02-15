
import re

def extract_hashtags(text):
    hashtags = re.findall(r"#(\w+)", text)
    return hashtags

text = "Hello world! #Python is a great programming language! #coding #programming"
hashtags = extract_hashtags(text)

print("Hashtags in the text:")
for hashtag in hashtags:
    print(hashtag)
