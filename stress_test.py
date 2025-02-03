
def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

text = "This is a sample sentence to count the occurrences of each word in this string. This is a sample string."
word_count = count_words(text)

for word, count in word_count.items():
    print(f"{word}: {count}")
