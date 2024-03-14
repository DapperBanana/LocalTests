
def find_replace_word(file_name, find_word, replace_word):
    with open(file_name, 'r') as file:
        filedata = file.read()

    new_filedata = filedata.replace(find_word, replace_word)

    with open(file_name, 'w') as file:
        file.write(new_filedata)

    print(f"Word '{find_word}' replaced with '{replace_word}' in the file.")

file_name = 'sample.txt'
find_word = 'old_word'
replace_word = 'new_word'

find_replace_word(file_name, find_word, replace_word)
