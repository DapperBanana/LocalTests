
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

if __name__ == "__main__":
    text = "Hello #world! This is a #test #program"
    hashtags = extract_hashtags(text)
    
    if hashtags:
        print("Hashtags found:")
        for hashtag in hashtags:
            print(hashtag)
    else:
        print("No hashtags found in the text.")
