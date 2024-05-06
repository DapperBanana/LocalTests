
def count_word_occurrences(string):
    word_list = string.split()
    word_counts = {}
    
    for word in word_list:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# Example usage
input_string = "This is a sample string with words. This is a sample string with words."
count_word_occurrences(input_string)
