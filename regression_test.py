letion(id='chatcmpl-9Cx7Q64bLbRZkTof7LDPK3i1pmh7o', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def is_harshad_number(num):
    # Calculate the sum of digits of the number
    sum_of_digits = sum(int(digit) for digit in str(num))
    
    # Check if the number is divisible by the sum of its digits
    return num % sum_of_digits == 0

# Test the function with some numbers
print(is_harshad_number(18)) # True
print(is_harshad_number(20)) # False
print(is_harshad_number(21)) # True
print(is_harshad_number(88)) # True
print(is_harshad_number(100)) # True', role='assistant', function_call=None, tool_calls=None))], created=1712874216, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_b28b39ffa8', usage=CompletionUsage(completion_tokens=135, prompt_tokens=28, total_tokens=163)