
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        print("File not found")
        return -1

file_name = 'sample.txt'
num_words = count_words(file_name)
if num_words != -1:
    print(f"Number of words in {file_name}: {num_words}")
