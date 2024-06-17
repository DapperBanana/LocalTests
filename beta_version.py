
def find_replace_word(file_name, word_to_find, replacement_word):
    # Open the file in read mode
    with open(file_name, 'r') as file:
        file_data = file.read()

    # Replace the word
    new_data = file_data.replace(word_to_find, replacement_word)

    # Open the file in write mode and write the new data
    with open(file_name, 'w') as file:
        file.write(new_data)

    print(f"Word '{word_to_find}' has been replaced with '{replacement_word}' in the file.")

# Enter the file name, word to find and replacement word
file_name = "sample.txt"
word_to_find = "old_word"
replacement_word = "new_word"

# Call the function to find and replace the word
find_replace_word(file_name, word_to_find, replacement_word)
