
def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

sentence = "This is a sample sentence to count the occurrences of each word in this sentence"
word_occurrences = count_word_occurrences(sentence)

for word, count in word_occurrences.items():
    print(f"{word}: {count}")
