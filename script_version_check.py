
def decimal_to_binary(decimal):
    if decimal > 1:
        decimal_to_binary(decimal // 2)
    print(decimal % 2, end='')

# take input from the user
decimal_num = int(input("Enter a decimal number: "))

# calling the function
decimal_to_binary(decimal_num)
