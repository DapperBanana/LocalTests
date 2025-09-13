
import re

def extract_hashtags(text):
    hashtags = re.findall(r"#(\w+)", text)
    return hashtags

if __name__ == "__main__":
    text = "I love #coding and #programming! #Python is my favorite language."
    hashtags = extract_hashtags(text)

    print("Hashtags found in the text:")
    for hashtag in hashtags:
        print(hashtag)
