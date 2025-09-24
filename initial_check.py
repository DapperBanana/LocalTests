
def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            print(f'Total number of words in the file "{file_name}" is: {num_words}')
    except FileNotFoundError:
        print(f'File named "{file_name}" not found.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        
file_name = 'sample.txt'
count_words_in_file(file_name)
