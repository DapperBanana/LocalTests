
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        print("File not found.")

file_name = "sample.txt"
word_count = count_words(file_name)
print(f"Number of words in the file '{file_name}': {word_count}")
