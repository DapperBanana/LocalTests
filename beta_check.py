
def count_words(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

file_name = 'sample.txt'
word_count = count_words(file_name)
print(f'The number of words in {file_name} is: {word_count}')
