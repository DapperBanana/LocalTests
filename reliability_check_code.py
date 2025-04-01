
def find_and_replace_word(file_name, old_word, new_word):
    with open(file_name, 'r') as file:
        file_data = file.read()

    file_data = file_data.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(file_data)
    
    print(f"Word '{old_word}' replaced with '{new_word}' in file '{file_name}'.")

file_name = 'example.txt'
old_word = 'old_word'
new_word = 'new_word'

find_and_replace_word(file_name, old_word, new_word)
