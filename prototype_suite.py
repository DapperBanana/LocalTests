
def is_harshad_number(num):
    num_str = str(num)
    digit_sum = sum(int(digit) for digit in num_str)
    
    return num % digit_sum == 0

num = int(input("Enter a number: "))

if is_harshad_number(num):
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshad number")
