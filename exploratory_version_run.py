
def count_words(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        return word_count

file_name = 'sample.txt'
num_words = count_words(file_name)
print(f"The number of words in {file_name} is: {num_words}")
