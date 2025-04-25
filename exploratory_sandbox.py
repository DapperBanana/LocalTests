
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

try:
    distance = hamming_distance(str1, str2)
    print(f"The Hamming distance between '{str1}' and '{str2}' is {distance}")
except ValueError as e:
    print(e)
