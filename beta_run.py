
def get_sum_of_digits(num):
    if num < 10:
        return num
    else:
        total = 0
        while num > 0:
            total += num % 10
            num = num // 10
        return get_sum_of_digits(total)

number = int(input("Enter a number: "))
result = get_sum_of_digits(number)
print("The sum of digits of the number until it becomes a single-digit number is:", result)
