
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        print("File not found.")
        return 0

file_name = 'sample.txt'
num_words = count_words(file_name)
print(f"Number of words in the file: {num_words}")
