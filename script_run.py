
def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
        
    if sum < 10:
        return sum
    else:
        return sum_of_digits(sum)

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("Sum of digits until it becomes a single-digit number:", result)
