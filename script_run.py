
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            print(f'The number of words in the file "{file_name}" is: {num_words}')
    except FileNotFoundError:
        print("File not found.")

file_name = 'sample.txt'
count_words(file_name)
