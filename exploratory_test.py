
def replace_word(file_name, word_to_replace, replacement_word):
    with open(file_name, 'r') as file:
        file_data = file.read()
    
    file_data = file_data.replace(word_to_replace, replacement_word)
    
    with open(file_name, 'w') as file:
        file.write(file_data)

file_name = 'sample.txt'
word_to_replace = 'old_word'
replacement_word = 'new_word'

replace_word(file_name, word_to_replace, replacement_word)

print(f'{word_to_replace} has been replaced with {replacement_word} in {file_name}.')
