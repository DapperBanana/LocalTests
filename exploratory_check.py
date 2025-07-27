
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            print(f"Number of words in {file_path}: {num_words}")
    except FileNotFoundError:
        print("File not found")

file_path = 'sample.txt'
count_words_in_file(file_path)
