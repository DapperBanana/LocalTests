
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length.")
    
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

# Example
str1 = "karolin"
str2 = "kathrin"
print("Hamming distance between {} and {} is {}".format(str1, str2, hamming_distance(str1, str2)))
