
def replace_word_in_file(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        file_data = file.read()

    new_file_data = file_data.replace(old_word, new_word)

    with open(file_path, 'w') as file:
        file.write(new_file_data)

file_path = 'sample.txt'
old_word = 'old_word'
new_word = 'new_word'

replace_word_in_file(file_path, old_word, new_word)
print(f"Word '{old_word}' replaced with '{new_word}' in '{file_path}'.")
