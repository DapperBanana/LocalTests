
def is_vampire_number(number):
    num_str = str(number)
    if len(num_str) % 2 != 0:
        return False
    
    fangs = []
    for perm in permutations(num_str):
        fang1 = int(''.join(perm[:len(num_str)//2]))
        fang2 = int(''.join(perm[len(num_str)//2:]))
        if fang1 * fang2 == number and fang1 % 10 != 0 and fang2 % 10 != 0:
            fangs.append((fang1, fang2))
    
    return fangs

def permutations(string):
    if len(string) == 1:
        return [string]
    
    perms = []
    for i in range(len(string)):
        before = string[:i]
        after = string[i+1:]
        for perm in permutations(before + after):
            perms.append(string[i] + perm)
    
    return perms

number = int(input("Enter a number: "))
result = is_vampire_number(number)

if result:
    print(f"{number} is a vampire number with fangs:")
    for fang1, fang2 in result:
        print(f"{fang1} * {fang2} = {number}")
else:
    print(f"{number} is not a vampire number.")
