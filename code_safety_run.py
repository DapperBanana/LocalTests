
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found"

file_name = 'sample.txt'  # Specify the name of the text file
word_count = count_words(file_name)
if type(word_count) == int:
    print(f'The file has {word_count} words.')
else:
    print(word_count)
