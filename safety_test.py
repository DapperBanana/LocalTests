letion(id='chatcmpl-8vEcIXDbNGTGNl87IcTGf5esI9JLh', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to calculate GCD of two numbers
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: ")

# Calculate GCD
result = gcd(num1, num2)

# Output
print(f"The GCD of {num1} and {num2} is: {result}")', role='assistant', function_call=None, tool_calls=None))], created=1708651574, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_cbdb91ce3f', usage=CompletionUsage(completion_tokens=101, prompt_tokens=25, total_tokens=126)