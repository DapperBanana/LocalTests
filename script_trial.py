
def find_replace(file_name, search_word, replace_word):
    with open(file_name, 'r') as file:
        data = file.read()

    new_data = data.replace(search_word, replace_word)

    with open(file_name, 'w') as file:
        file.write(new_data)

    print(f"'{search_word}' replaced with '{replace_word}' in {file_name}.")

# Provide the file name, word to search for, and word to replace with
file_name = 'sample.txt'
search_word = 'old_word'
replace_word = 'new_word'

find_replace(file_name, search_word, replace_word)
