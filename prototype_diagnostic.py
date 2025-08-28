
def count_word_occurrences(text):
    words = text.split()
    word_count = {}
    
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

text = "Hello world, hello there. How are you today? Hello world!"
word_count = count_word_occurrences(text)

for word, count in word_count.items():
    print(f"'{word}' occurs {count} times.")
