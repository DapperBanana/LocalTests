
from collections import Counter

def count_words(string):
    words = string.split()
    word_count = Counter(words)
    return word_count

string = "hello world hello python world"
word_count = count_words(string)

for word, count in word_count.items():
    print(f"{word}: {count}")
