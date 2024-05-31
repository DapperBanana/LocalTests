
def find_replace_word(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        text = file.read()
    
    text = text.replace(old_word, new_word)
    
    with open(file_path, 'w') as file:
        file.write(text)
    
    print(f"'{old_word}' replaced with '{new_word}' in '{file_path}'.")

file_path = 'sample.txt'
old_word = 'Python'
new_word = 'Java'

find_replace_word(file_path, old_word, new_word)
