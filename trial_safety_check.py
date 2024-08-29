
def is_vampire_number(num):
    num_str = str(num)
    if len(num_str) % 2 != 0:
        return False

    digits = [int(d) for d in num_str]
    for i in range(10**(len(num_str)//2 - 1), int(num**0.5)+1):
        if num % i == 0:
            fangs = str(i) + str(num//i)
            if sorted(fangs) == sorted(num_str):
                return True

    return False

num = int(input("Enter a number: "))
if is_vampire_number(num):
    print(f"{num} is a vampire number.")
else:
    print(f"{num} is not a vampire number.")
