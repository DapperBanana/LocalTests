
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            distance += 1
    
    return distance

# Test the function
string1 = "karolin"
string2 = "kathrin"
print("Hamming distance between '{}' and '{}' is: {}".format(
    string1, string2, hamming_distance(string1, string2)))
