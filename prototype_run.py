
def find_replace_word(file_name, old_word, new_word):
    with open(file_name, 'r') as file:
        data = file.read()

    replaced_data = data.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(replaced_data)

file_name = "sample.txt"
old_word = "old_word"
new_word = "new_word"

find_replace_word(file_name, old_word, new_word)
