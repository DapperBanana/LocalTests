
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

# Input text
text = "Check out this amazing new #Python program for extracting hashtags! #programming #coding #hashtags"

# Extract hashtags from the text
hashtags = extract_hashtags(text)

# Print the extracted hashtags
print("Extracted hashtags:")
for hashtag in hashtags:
    print(hashtag)
