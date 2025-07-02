
def find_replace_word(file_name, word_to_find, word_to_replace):
    with open(file_name, 'r') as file:
        file_content = file.read()

    new_content = file_content.replace(word_to_find, word_to_replace)

    with open(file_name, 'w') as file:
        file.write(new_content)

# Replace 'old_word' with 'new_word' in 'sample.txt' file
find_replace_word('sample.txt', 'old_word', 'new_word')
