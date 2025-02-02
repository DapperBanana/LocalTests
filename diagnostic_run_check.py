
def is_perfect_square(num):
    if num < 0:
        return False
    elif num == 0:
        return True
    else:
        i = 1
        while i*i <= num:
            if i*i == num:
                return True
            i += 1
        return False

num = int(input("Enter a number: "))
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
