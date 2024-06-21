
def count_words(string):
    word_count = {}
    
    # Split the string into words
    words = string.split()
    
    # Count the occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Input string
input_string = "This is a sample string with several words and some repeated words"

# Count the occurrences of each word in the input string
word_count = count_words(input_string)

# Print the result
for word, count in word_count.items():
    print(f"{word}: {count}")
