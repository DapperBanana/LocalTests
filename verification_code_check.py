
def find_square_root(number):
    if number < 0:
        return "Square root is not defined for negative numbers"
    
    guess = number / 2
    tolerance = 0.0001
    
    while abs((guess ** 2) - number) > tolerance:
        guess = (guess + number / guess) / 2
    
    return round(guess, 4)

number = float(input("Enter a number: "))
square_root = find_square_root(number)

print(f"The square root of {number} is {square_root}")
