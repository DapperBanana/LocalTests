
def convert_base(num, from_base=10, to_base=10):
    if from_base == 10:
        return int(num, to_base)
    else:
        return format(int(num, from_base), f'0{to_base}b')

number = input("Enter the number you want to convert: ")
from_base = int(input("Enter the base of the number you entered: "))
to_base = int(input("Enter the base you want to convert to: "))

result = convert_base(number, from_base, to_base)
print(f'{number} in base {from_base} is {result} in base {to_base}')
