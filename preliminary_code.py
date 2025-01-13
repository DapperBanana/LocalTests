
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

text = "Hello #world! Here are some #hashtags for #Python programming."
hashtags = extract_hashtags(text)
print(hashtags)
