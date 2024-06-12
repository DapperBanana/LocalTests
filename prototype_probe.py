
def find_replace_word(file_name, word_to_find, word_to_replace):
    with open(file_name, 'r') as file:
        text = file.read()

    text = text.replace(word_to_find, word_to_replace)

    with open(file_name, 'w') as file:
        file.write(text)

file_name = 'sample.txt'
word_to_find = 'old_word'
word_to_replace = 'new_word'

find_replace_word(file_name, word_to_find, word_to_replace)
