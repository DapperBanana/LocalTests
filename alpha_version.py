
def count_words(input_string):
    word_count = {}
    words = input_string.split()

    for word in words:
        word = word.lower()
        word = word.strip(",.")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


input_string = "Hello world, hello python world"
word_occurrences = count_words(input_string)

for word, count in word_occurrences.items():
    print(f"{word}: {count}")
