
def count_words(sentence):
    word_count = {}
    
    for word in sentence.split():
        word = word.lower()
        word = ''.join(e for e in word if e.isalnum())  # remove non-alphanumeric characters from the word
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Test the function
sentence = "Hello, world! Hello, Python! Python is a great programming language."
count_words(sentence)
