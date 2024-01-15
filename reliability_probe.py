
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return -1

# Example usage
filename = 'sample.txt'
word_count = count_words(filename)

if word_count != -1:
    print(f"Number of words in '{filename}': {word_count}")
