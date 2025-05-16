
def count_word_occurrences(input_string):
    word_count = {}
    
    words = input_string.split()
    
    for word in words:
        word = word.lower()
        word = word.strip(",.!?")
        
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

input_string = "Hello there, how are you? Are you doing well?"
word_occurrences = count_word_occurrences(input_string)

for word, count in word_occurrences.items():
    print(f"{word}: {count}")
