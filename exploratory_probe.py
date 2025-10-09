
def count_words(string):
    words = string.split()
    word_count = {}
    
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

input_string = "This is a test string to test the word count program. Test it yourself."
word_count = count_words(input_string)

for word, count in word_count.items():
    print(f'{word}: {count}')
