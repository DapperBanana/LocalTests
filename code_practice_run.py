
def count_words_in_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        print("File not found.")
        return None

file_path = 'sample.txt'
num_words = count_words_in_text_file(file_path)
if num_words:
    print(f"Number of words in file '{file_path}': {num_words}")
