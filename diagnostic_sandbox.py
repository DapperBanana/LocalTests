
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

filename = input("Enter the name of the text file: ")
word_count = count_words(filename)
if word_count is not None:
    print(f"There are {word_count} words in the file '{filename}'.")
