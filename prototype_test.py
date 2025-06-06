
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

if __name__ == "__main__":
    text = "This is a sample text with #hashtags and #morehashtags"
    hashtags = extract_hashtags(text)
    print(hashtags)
