
def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            print(f'The number of words in the file {file_name} is: {num_words}')
    except FileNotFoundError:
        print(f'File {file_name} not found.')

file_name = 'sample.txt'  # Enter the name of the text file here
count_words_in_file(file_name)
