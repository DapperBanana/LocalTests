
def count_words(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the contents of the file
            text = file.read()

            # Split the text by whitespace to get a list of words
            words = text.split()

            # Count the number of words in the list
            word_count = len(words)

            return word_count
    except FileNotFoundError:
        return "File not found"

# Provide the file path of the text file
file_path = "path/to/text_file.txt"

# Call the function and print the result
result = count_words(file_path)
print("Number of words:", result)
