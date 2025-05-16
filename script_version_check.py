
def count_words(string):
    words = string.split()
    word_count = {}
    
    for word in words:
        # Remove punctuation and convert to lowercase
        word = word.strip('.,!?"\'').lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

string = "This is a sample string, hello world. Sample string!"
word_count = count_words(string)

for word, count in word_count.items():
    print(f"'{word}': {count}")
