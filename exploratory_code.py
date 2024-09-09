
def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        return "File not found"

file_path = 'your_text_file.txt'
num_words = count_words(file_path)
print(f'Number of words in the file: {num_words}')
