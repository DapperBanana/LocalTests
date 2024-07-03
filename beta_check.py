
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")

    distance = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1

    return distance

# Test the function
str1 = "karolin"
str2 = "kathrin"
print(f"The Hamming distance between '{str1}' and '{str2}' is: {hamming_distance(str1, str2)}")
