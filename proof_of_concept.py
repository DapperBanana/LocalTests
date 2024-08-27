
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

text = "Hello friends, check out this #awesome python program! I love coding with #hashtags #python"

hashtags = extract_hashtags(text)
for hashtag in hashtags:
    print(hashtag)
