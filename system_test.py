
def count_words(string):
    words = string.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        print(f'{word}: {count}')

# Test the function
string = "hello world hello python world"
count_words(string)
