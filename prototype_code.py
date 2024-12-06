
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags

text = "Hello #world, it's a beautiful day! #nature #sunny #happy"
hashtags = extract_hashtags(text)
print(hashtags)
