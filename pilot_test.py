
def find_replace_word(input_file, output_file, old_word, new_word):
    with open(input_file, 'r') as file:
        file_data = file.read()
    
    file_data = file_data.replace(old_word, new_word)
    
    with open(output_file, 'w') as file:
        file.write(file_data)

input_file = 'input.txt'
output_file = 'output.txt'
old_word = 'hello'
new_word = 'goodbye'

find_replace_word(input_file, output_file, old_word, new_word)

print(f"{old_word} replaced with {new_word} in the file.")
