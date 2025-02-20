
import re

def extract_hashtags(text):
    hashtags = re.findall(r"#(\w+)", text)
    return hashtags

text = "Check out this #beautiful sunset! #nature #photography #nofilter"
hashtags = extract_hashtags(text)

print("Hashtags found in the text:")
for hashtag in hashtags:
    print("#" + hashtag)
