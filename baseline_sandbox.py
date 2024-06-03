
def number_to_roman(num):
    roman_numeral = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    
    result = ''
    for key in sorted(roman_numeral.keys(), reverse=True):
        while num >= key:
            result += roman_numeral[key]
            num -= key
    
    return result

num = int(input("Enter a number: "))
print("Roman numeral:", number_to_roman(num))
