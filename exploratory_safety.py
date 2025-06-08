
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            total_words = len(words)
            
            if total_words == 1:
                print(f'There is 1 word in the file.')
            else:
                print(f'There are {total_words} words in the file.')
    except FileNotFoundError:
        print("File not found.")

file_name = 'example.txt'
count_words(file_name)
