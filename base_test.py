
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

text = "I love #coding and #programming! #Python is my favorite language."
hashtags = extract_hashtags(text)

print("Hashtags: ", hashtags)
