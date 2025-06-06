
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            words = data.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        print("File not found.")
        return None

file_path = "sample.txt"  # Change this to the path of your text file
num_words = count_words_in_file(file_path)

if num_words is not None:
    print(f"The number of words in the file is: {num_words}")
