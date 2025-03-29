
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        num_words = len(words)
    return num_words

file_path = 'sample_text.txt'
word_count = count_words(file_path)
print(f'Total number of words in the file: {word_count}')
