
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags

text = "Hello #world, how are you doing? #Python is awesome!"
hashtags_list = extract_hashtags(text)

for hashtag in hashtags_list:
    print(hashtag)
