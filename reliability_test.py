
def find_replace_word(file_name, find_word, replace_word):
    with open(file_name, 'r') as file:
        file_contents = file.read()

    new_contents = file_contents.replace(find_word, replace_word)

    with open(file_name, 'w') as file:
        file.write(new_contents)

file_name = 'sample.txt'
find_word = 'old_word'
replace_word = 'new_word'

find_replace_word(file_name, find_word, replace_word)
