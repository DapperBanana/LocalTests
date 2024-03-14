
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

filename = 'sample_text.txt'
word_count = count_words(filename)
print(f'The number of words in the file "{filename}" is: {word_count}')
