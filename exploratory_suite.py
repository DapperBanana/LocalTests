
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            print(f'The number of words in {file_name} is: {num_words}')
    except FileNotFoundError:
        print(f'Error: File {file_name} not found')

file_name = 'sample.txt'  # Update with the name of the text file
count_words(file_name)
