
def find_replace_word(file_name, word_to_find, replace_with):
    with open(file_name, 'r') as file:
        text = file.read()

    new_text = text.replace(word_to_find, replace_with)

    with open(file_name, 'w') as file:
        file.write(new_text)

file_name = 'example.txt'
word_to_find = 'old_word'
replace_with = 'new_word'

find_replace_word(file_name, word_to_find, replace_with)
print(f'{word_to_find} replaced with {replace_with} in {file_name}')
