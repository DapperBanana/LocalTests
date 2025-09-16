
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            print(f"The number of words in the file {filename} is: {num_words}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Replace 'example.txt' with the name of the text file you want to count the words in
count_words('example.txt')
