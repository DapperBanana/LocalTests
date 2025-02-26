
def count_words(filename):
    with open(filename, 'r') as file:
        data = file.read()
        words = data.split()
        num_words = len(words)
        return num_words

filename = 'sample_text.txt'
num_words = count_words(filename)
print(f'The number of words in the file {filename} is: {num_words}')
