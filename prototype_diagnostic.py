
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print("File not found")
        return 0

file_name = "text_file.txt"
num_words = count_words(file_name)
print(f"Number of words in {file_name}: {num_words}")
