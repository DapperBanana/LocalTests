
def find_replace(file_name, word_to_replace, replacement_word):
    with open(file_name, 'r') as file:
        file_content = file.read()

    new_content = file_content.replace(word_to_replace, replacement_word)

    with open(file_name, 'w') as file:
        file.write(new_content)

file_name = 'sample_text.txt'
word_to_replace = 'old_word'
replacement_word = 'new_word'

find_replace(file_name, word_to_replace, replacement_word)
print(f'{word_to_replace} replaced with {replacement_word} in {file_name}')
