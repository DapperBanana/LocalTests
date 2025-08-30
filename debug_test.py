
def is_harshad_number(num):
    if num <= 0:
        return False

    digit_sum = sum(int(digit) for digit in str(num))
    
    return num % digit_sum == 0


number = int(input("Enter a number: "))
if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
