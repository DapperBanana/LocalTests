
import re

def extract_hashtags(text):
    hashtags = re.findall(r"#(\w+)", text)
    return hashtags

text = "This is a sample text with #hashtags and #Python. #programming is fun!"
hashtags = extract_hashtags(text)

print("Hashtags found in the text:")
for hashtag in hashtags:
    print(hashtag)
