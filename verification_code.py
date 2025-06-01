
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
        
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
            
    return distance

# Test the function
str1 = "karolin"
str2 = "kathrin"
print(hamming_distance(str1, str2))  # Output: 3
