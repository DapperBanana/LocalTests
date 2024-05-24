
def find_and_replace(file_name, target_word, replacement_word):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    with open(file_name, 'w') as file:
        for line in lines:
            new_line = line.replace(target_word, replacement_word)
            file.write(new_line)
    
    print(f"Word '{target_word}' replaced with '{replacement_word}' in file '{file_name}'.")


file_name = 'sample.txt'
target_word = 'old_word'
replacement_word = 'new_word'

find_and_replace(file_name, target_word, replacement_word)
