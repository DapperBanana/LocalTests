
def find_and_replace(file_name, word_to_find, word_to_replace):
    with open(file_name, 'r') as file:
        file_data = file.read()

    new_file_data = file_data.replace(word_to_find, word_to_replace)
    
    with open(file_name, 'w') as file:
        file.write(new_file_data)

    print(f"Word '{word_to_find}' replaced with '{word_to_replace}' in {file_name}")

file_name = "example.txt"
word_to_find = "old_word"
word_to_replace = "new_word"

find_and_replace(file_name, word_to_find, word_to_replace)
