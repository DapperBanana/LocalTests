
def replace_word(file_name, old_word, new_word):
    try:
        with open(file_name, 'r') as file:
            text = file.read()

        # Replace the old word with the new word
        new_text = text.replace(old_word, new_word)

        with open(file_name, 'w') as file:
            file.write(new_text)

        print(f"The word '{old_word}' has been replaced with '{new_word}' in the file '{file_name}'.")
    
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

# Example usage
replace_word('example.txt', 'apple', 'orange')
