
def count_word_occurrences(text):
    words = text.split()
    word_count = {}
    
    # Count occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Test the function
text = "hello world hello python world"
result = count_word_occurrences(text)
for word, count in result.items():
    print(f"{word}: {count}")
