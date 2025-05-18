
def count_word_occurrences(input_string):
    word_list = input_string.split()
    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

input_string = "hello world hello python world"
word_occurrences = count_word_occurrences(input_string)

for word, count in word_occurrences.items():
    print(f"{word}: {count}")
