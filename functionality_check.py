
def find_replace_word(file_name, old_word, new_word):
    with open(file_name, 'r') as file:
        file_data = file.read()

    new_file_data = file_data.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(new_file_data)

# Prompt user for file name, word to find, and word to replace
file_name = input("Enter the file name: ")
old_word = input("Enter the word to find: ")
new_word = input("Enter the word to replace it with: ")

find_replace_word(file_name, old_word, new_word)

print("Word replaced successfully.")
