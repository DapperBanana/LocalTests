
import re

def extract_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags

if __name__ == "__main__":
    text = "Check out this #awesome Python program! #coding #hashtags #programming"
    hashtags = extract_hashtags(text)
    
    if hashtags:
        print("Hashtags found in the text:")
        for tag in hashtags:
            print(tag)
    else:
        print("No hashtags found in the text.")
