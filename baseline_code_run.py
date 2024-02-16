letion(id='chatcmpl-8sxiZyvWjnfNX5YCgFvBrt0eAAmLo', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="'''
A Harshad (Niven) number is an integer that is divisible by the sum of its digits.
'''

def is_harshad_number(number):
    # Find the sum of the digits
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    
    # Check if the number is divisible by the sum of its digits
    if number % sum_digits == 0:
        return True
    else:
        return False


# Test the function with some example numbers
print(is_harshad_number(18))  # True
print(is_harshad_number(10))  # True
print(is_harshad_number(21))  # False
print(is_harshad_number(124)) # False
print(is_harshad_number(156)) # True
print(is_harshad_number(201)) # True
print(is_harshad_number(333)) # True
print(is_harshad_number(625)) # False
print(is_harshad_number(7128)) # False
print(is_harshad_number(9999)) # False", role='assistant', function_call=None, tool_calls=None))], created=1708109959, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=244, prompt_tokens=28, total_tokens=272)