
def isPerfectSquare(num):
    if num < 0:
        return False
        
    i = 0
    while i*i <= num:
        if i*i == num:
            return True
        i += 1
        
    return False

# test the function
num = int(input("Enter a number: "))
if isPerfectSquare(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
