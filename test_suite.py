
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

text = "This is a sample text with #hashtags #python #programming"
hashtags = extract_hashtags(text)

print("All hashtags in the text are:")
for hashtag in hashtags:
    print(hashtag)
