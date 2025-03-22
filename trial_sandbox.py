
def find_replace(file_name, word_to_find, word_to_replace):
    with open(file_name, 'r') as file:
        filedata = file.read()

    newdata = filedata.replace(word_to_find, word_to_replace)

    with open(file_name, 'w') as file:
        file.write(newdata)

file_name = 'sample.txt'
word_to_find = 'old_word'
word_to_replace = 'new_word'

find_replace(file_name, word_to_find, word_to_replace)

print(f"{word_to_find} has been replaced with {word_to_replace} in {file_name}")
