
def count_words(string):
    word_count = {}
    
    words = string.split()
    
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

string = "hello world hello python python"
word_counts = count_words(string)

for word, count in word_counts.items():
    print(f"{word}: {count}")
