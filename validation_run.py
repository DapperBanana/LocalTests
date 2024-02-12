
def find_replace_word(file_path, old_word, new_word):
    # Read the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Replace the old word with the new word
    new_text = text.replace(old_word, new_word)

    # Write the updated text back to the file
    with open(file_path, 'w') as file:
        file.write(new_text)

    print("Word replacement complete.")


# Example usage
file_path = "example.txt"  # Path to the text file
old_word = "old_word"     # Word to find
new_word = "new_word"     # Word to replace with

find_replace_word(file_path, old_word, new_word)
