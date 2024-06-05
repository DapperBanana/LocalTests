
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            word_count = len(data.split())
            print(f'Number of words in {file_name}: {word_count}')
    except FileNotFoundError:
        print(f'Error: {file_name} not found')

# Replace 'example.txt' with the name of your text file
file_name = 'example.txt'
count_words(file_name)
