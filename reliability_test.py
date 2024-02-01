
def find_replace_file(filename, word_to_find, replacement):
    with open(filename, 'r') as file:
        content = file.read()

    new_content = content.replace(word_to_find, replacement)

    with open(filename, 'w') as file:
        file.write(new_content)

    print(f"Word '{word_to_find}' replaced with '{replacement}' in {filename}")


# Example usage:
file_name = "example.txt"
word_to_find = "oldword"
replacement = "newword"

find_replace_file(file_name, word_to_find, replacement)
