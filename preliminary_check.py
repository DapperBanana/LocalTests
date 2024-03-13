
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags

text = "This is a sample text with #hashtags and some #morehashtags"
hashtags = extract_hashtags(text)

print("Extracted hashtags:")
for tag in hashtags:
    print(tag)
