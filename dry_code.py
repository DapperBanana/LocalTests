
def count_words(string):
    # Remove punctuations and convert string to lowercase
    string = string.lower()
    string = ''.join(c for c in string if c.isalnum() or c.isspace())
    
    # Split the string into words
    words = string.split()
    
    # Create an empty dictionary to store word counts
    word_counts = {}
    
    # Count the occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Print the word counts
    for word, count in word_counts.items():
        print(word, ':', count)
        
# Test the function
string = input("Enter a string: ")
count_words(string)
