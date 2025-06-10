
def find_and_replace_word(file_name, target_word, replacement_word):
    with open(file_name, 'r') as file:
        content = file.read()

    modified_content = content.replace(target_word, replacement_word)

    with open(file_name, 'w') as file:
        file.write(modified_content)

    print(f"Word '{target_word}' replaced with '{replacement_word}' in '{file_name}'.")

# Replace 'old_word' with 'new_word' in 'example.txt' file
find_and_replace_word('example.txt', 'old_word', 'new_word')
