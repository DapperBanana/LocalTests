
def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            print(f"The number of words in the file '{file_name}' is {num_words}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = 'sample.txt'  # Change this to the name of your file
count_words_in_file(file_name)
