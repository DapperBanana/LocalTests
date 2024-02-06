
def count_words(string):
    # converting string to lowercase and splitting it into words
    words = string.lower().split()
    
    # creating an empty dictionary to store word count
    word_count = {}
    
    # counting occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# testing the program
string = "I am a Python programmer. I am learning Python programming."
result = count_words(string)
print(result)
