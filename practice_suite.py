
def roman_to_int(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_num = 0
    
    for i in range(len(roman_numeral)):
        if i > 0 and roman_dict[roman_numeral[i]] > roman_dict[roman_numeral[i-1]]:
            int_num += roman_dict[roman_numeral[i]] - 2*roman_dict[roman_numeral[i-1]]
        else:
            int_num += roman_dict[roman_numeral[i]]
    
    return int_num

roman_numeral = input("Enter a Roman numeral: ")
print(f"The equivalent integer value is: {roman_to_int(roman_numeral)}")
