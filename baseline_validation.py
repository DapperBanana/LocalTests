
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    
    return count

str1 = "abc"
str2 = "abd"
print(hamming_distance(str1, str2))  # Output: 1
