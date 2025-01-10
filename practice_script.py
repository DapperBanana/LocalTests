
def find_replace_word(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        text = file.read()

    updated_text = text.replace(old_word, new_word)

    with open(file_path, 'w') as file:
        file.write(updated_text)

    print(f"Word '{old_word}' replaced with '{new_word}' in file {file_path}")

# Provide the file path, old word, and the new word to replace
file_path = 'sample.txt'
old_word = 'old_word'
new_word = 'new_word'

find_replace_word(file_path, old_word, new_word)
