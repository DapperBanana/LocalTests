
def find_replace_word(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        text = file.read()
    
    updated_text = text.replace(old_word, new_word)
    
    with open(file_path, 'w') as file:
        file.write(updated_text)
    
    print(f"Word '{old_word}' replaced with '{new_word}' in the file '{file_path}'.")

# Replace 'old_word' with 'new_word' in 'input.txt' file
find_replace_word('input.txt', 'old_word', 'new_word')
