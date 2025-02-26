
def find_replace_word(file_name, find_word, replace_word):
    with open(file_name, 'r') as file:
        text = file.read()

    new_text = text.replace(find_word, replace_word)

    with open(file_name, 'w') as file:
        file.write(new_text)

    print(f"Word '{find_word}' replaced with '{replace_word}' in the file.")

# Example
file_name = 'example.txt'
find_word = 'old'
replace_word = 'new'

find_replace_word(file_name, find_word, replace_word)
