
def count_words(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        num_words = len(words)
    return num_words

file_name = 'sample_text.txt'
num_words = count_words(file_name)
print(f'The number of words in {file_name} is: {num_words}')
