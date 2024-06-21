
from collections import defaultdict

def count_occurrences(s):
    occurrences = defaultdict(int)
    for char in s:
        occurrences[char] += 1
    return occurrences

input_string = input("Enter a string: ")
occurrences = count_occurrences(input_string)

for char, count in occurrences.items():
    print(f"{char}: {count}")
