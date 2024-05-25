
def count_words(input_string):
    word_count = {}
    words = input_string.split()
    
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Test the function
input_string = "Hello world Python is Fun hello hello"
count_words(input_string)
