
def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    for i in range(len(roman)):
        if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i - 1]]:
            result += roman_dict[roman[i]] - 2 * roman_dict[roman[i - 1]]
        else:
            result += roman_dict[roman[i]]
    
    return result

# Test the function
print(roman_to_int("III")) # Output: 3
print(roman_to_int("IV")) # Output: 4
print(roman_to_int("IX")) # Output: 9
print(roman_to_int("LVIII")) # Output: 58
print(roman_to_int("MCMXCIV")) # Output: 1994
