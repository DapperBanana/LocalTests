
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {e}"
        
# Replace 'file.txt' with the path to the text file you want to count the words in
file_path = 'file.txt'
word_count = count_words_in_file(file_path)

if isinstance(word_count, int):
    print(f"The file '{file_path}' contains {word_count} words.")
else:
    print(word_count)
