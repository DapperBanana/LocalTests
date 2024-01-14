
def find_replace_word(file_name, old_word, new_word):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            # Replace the word
            updated_data = data.replace(old_word, new_word)
        
        with open(file_name, 'w') as file:
            # Write the updated data back to the file
            file.write(updated_data)
        
        print(f"Successfully replaced '{old_word}' with '{new_word}' in {file_name}.")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    old_word = input("Enter the word to be replaced: ")
    new_word = input("Enter the new word: ")

    find_replace_word(file_name, old_word, new_word)
