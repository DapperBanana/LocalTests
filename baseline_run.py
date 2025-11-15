
def find_and_replace(file_name, find_word, replace_word):
    with open(file_name, 'r') as file:
        data = file.read()

    data = data.replace(find_word, replace_word)

    with open(file_name, 'w') as file:
        file.write(data)

    print(f'{find_word} replaced with {replace_word} in {file_name}')

file_name = 'sample.txt'
find_word = 'old_word'
replace_word = 'new_word'

find_and_replace(file_name, find_word, replace_word)
