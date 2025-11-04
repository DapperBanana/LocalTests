
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags

text = "Hello #world! This is a sample #text with #hashtags. #Python #programming"

hashtags = extract_hashtags(text)

print("Extracted hashtags:", hashtags)
