
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

# Example text
text = "Check out this cool #python program for extracting #hashtags from text #coding"

# Extract hashtags
hashtags = extract_hashtags(text)

# Print extracted hashtags
for hashtag in hashtags:
    print(hashtag)
