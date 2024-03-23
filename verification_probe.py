
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)

file_path = "sample.txt"
word_count = count_words_in_file(file_path)
if word_count:
    print("Number of words in the file:", word_count)
