
def find_replace_word(file_name, old_word, new_word):
    with open(file_name, 'r') as file:
        file_data = file.read()

    file_data = file_data.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(file_data)

file_name = 'sample.txt'
old_word = 'apple'
new_word = 'banana'

find_replace_word(file_name, old_word, new_word)

print(f'{old_word} replaced with {new_word} in {file_name}')
