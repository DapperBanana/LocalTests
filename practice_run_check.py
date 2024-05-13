
def is_vampire_number(number):
    fangs = []
    number_str = str(number)
    
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factor1 = str(i)
            factor2 = str(number // i)
            
            if sorted(factor1 + factor2) == sorted(number_str):
                fangs.append((factor1, factor2))

    return fangs

number = 1260
fangs = is_vampire_number(number)

if fangs:
    print(f"{number} is a vampire number.")
    for fang in fangs:
        print(f"Fangs: {fang[0]} and {fang[1]}")
else:
    print(f"{number} is not a vampire number.")
