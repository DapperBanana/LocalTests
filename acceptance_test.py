
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        print("File not found")
        return -1

filename = 'sample.txt'
num_words = count_words(filename)
if num_words != -1:
    print(f"The number of words in the file '{filename}' is: {num_words}")
