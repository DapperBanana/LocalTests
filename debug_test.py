
def romanToInt(s):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s:
        value = roman_dict.get(char)
        total += value
        if value > prev_value:
            total -= 2 * prev_value
        prev_value = value
        
    return total

roman_numeral = input("Enter a Roman numeral: ")
print(f"The integer value of {roman_numeral} is: {romanToInt(roman_numeral)}")
