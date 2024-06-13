
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("The two strings must have the same length.")
    
    distance = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1
    
    return distance

# Input strings
str1 = "karolin"
str2 = "kathrin"

# Calculate and print Hamming distance
print("Hamming distance between '{}' and '{}': {}".format(str1, str2, hamming_distance(str1, str2)))
