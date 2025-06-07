
def count_words(text):
    words = text.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

text = "Hello world hello"
word_count = count_words(text)

for word, count in word_count.items():
    print(f"{word}: {count}")
