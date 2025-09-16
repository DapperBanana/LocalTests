
def find_replace_word(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        text = file.read()

    new_text = text.replace(old_word, new_word)

    with open(file_path, 'w') as file:
        file.write(new_text)

    print(f"Word '{old_word}' replaced with '{new_word}' in {file_path}")

# Specify the file path, old word and new word
file_path = 'example.txt'
old_word = 'old_word'
new_word = 'new_word'

find_replace_word(file_path, old_word, new_word)
