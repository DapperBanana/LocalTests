
def find_replace_word(file_name, old_word, new_word):
    with open(file_name, 'r') as file:
        text = file.read()

    new_text = text.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(new_text)

file_name = 'sample.txt'
old_word = 'old_word'
new_word = 'new_word'

find_replace_word(file_name, old_word, new_word)

print(f'{old_word} has been replaced with {new_word} in the file.')
