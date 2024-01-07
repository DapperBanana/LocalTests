
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            print("The number of words in the file is:", word_count)
    except FileNotFoundError:
        print("File not found.")

filename = input("Enter the name of the text file: ")
count_words(filename)
