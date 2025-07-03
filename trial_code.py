
def replace_word(file_name, old_word, new_word):
    with open(file_name, 'r') as file:
        text = file.read()

    updated_text = text.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(updated_text)

file_name = 'sample.txt'
old_word = 'old_word'
new_word = 'new_word'

replace_word(file_name, old_word, new_word)
