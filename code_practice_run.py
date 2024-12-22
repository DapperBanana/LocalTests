
def find_replace_word(file_name, old_word, new_word):
    with open(file_name, 'r') as file:
        text = file.read()

    new_text = text.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(new_text)

file_name = 'sample.txt'  # Name of the text file
old_word = 'old_word'  # Word to be replaced
new_word = 'new_word'  # Word to replace the old word with

find_replace_word(file_name, old_word, new_word)

print(f"Word '{old_word}' replaced with '{new_word}' in '{file_name}'")
