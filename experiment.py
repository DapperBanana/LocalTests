
def isHarshad(n):
    sum_digits = sum(int(i) for i in str(n))
    return n % sum_digits == 0

num = int(input("Enter a number: "))
if isHarshad(num):
    print(f"{num} is a Harshad (Niven) number.")
else:
    print(f"{num} is not a Harshad (Niven) number.")
