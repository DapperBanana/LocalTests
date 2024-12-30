
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags

text = "Check out this #amazing photo from my #vacation #trip #beautiful #scenery"
hashtags = extract_hashtags(text)

print("Hashtags found in the text:")
for tag in hashtags:
    print("#" + tag)
