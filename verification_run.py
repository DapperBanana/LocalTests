
def decimal_to_binary(decimal):
    binary = "{0:b}".format(decimal)
    return binary

# Input from user
decimal = int(input("Enter a decimal number: "))
binary = decimal_to_binary(decimal)

print(f"The binary representation of {decimal} is: {binary}")
