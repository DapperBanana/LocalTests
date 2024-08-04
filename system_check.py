
def find_replace(file_name, word_to_replace, new_word):
    with open(file_name, 'r') as file:
        data = file.read()
    
    modified_data = data.replace(word_to_replace, new_word)
    
    with open(file_name, 'w') as file:
        file.write(modified_data)
    
    print(f"Word '{word_to_replace}' replaced with '{new_word}' in '{file_name}'.")

file_name = 'example.txt'
word_to_replace = 'old_word'
new_word = 'new_word'

find_replace(file_name, word_to_replace, new_word)

# Verify the change
with open(file_name, 'r') as file:
    print(file.read())
