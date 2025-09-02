
def count_words(string):
    word_count = {}
    words = string.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(f'{word}: {count}')

# Example usage
string = "the quick brown fox jumps over the lazy dog"
count_words(string)
