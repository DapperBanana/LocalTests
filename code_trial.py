
def is_harshad_number(n):
    sum_of_digits = sum([int(digit) for digit in str(n)])
    return n % sum_of_digits == 0

# Test the function with some examples
num1 = 18
num2 = 20
num3 = 24

print(f"{num1} is a Harshad number: {is_harshad_number(num1)}")
print(f"{num2} is a Harshad number: {is_harshad_number(num2)}")
print(f"{num3} is a Harshad number: {is_harshad_number(num3)}")
