
def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("The two strings must have the same length")
    distance = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            distance += 1
    return distance

# Input two strings
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Calculate the Hamming distance
distance = hamming_distance(s1, s2)
print(f"The Hamming distance between '{s1}' and '{s2}' is {distance}")
