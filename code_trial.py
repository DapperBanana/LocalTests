
def find_replace(file_name, old_word, new_word):
    with open(file_name, 'r') as file:
        file_data = file.read()

    new_data = file_data.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(new_data)

file_name = 'sample.txt'
old_word = 'old_word'
new_word = 'new_word'

find_replace(file_name, old_word, new_word)
print(f'Replaced {old_word} with {new_word} in {file_name}')
