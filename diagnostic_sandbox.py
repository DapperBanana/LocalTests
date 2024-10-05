
def find_replace_word(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        text = file.read()

    modified_text = text.replace(old_word, new_word)

    with open(file_path, 'w') as file:
        file.write(modified_text)

    print(f"Word '{old_word}' replaced with '{new_word}' in '{file_path}'")


file_path = 'sample.txt'
old_word = 'old_word'
new_word = 'new_word'

find_replace_word(file_path, old_word, new_word)
