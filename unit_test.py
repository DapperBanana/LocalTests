letion(id='chatcmpl-9kfrHMIKf7XvMGRzC5NN2E6PS49Xj', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def is_perfect_digital_invariant(num):
    num_str = str(num)
    digit_sum = 0
    
    for digit in num_str:
        digit_sum += int(digit)
    
    if digit_sum * len(num_str) == num:
        return True
    else:
        return False

# Test the function with some examples
print(is_perfect_digital_invariant(18))  # True, 1+8 = 9, 9*2 = 18
print(is_perfect_digital_invariant(202))  # True, 2+0+2 = 4, 4*3 = 12
print(is_perfect_digital_invariant(123))  # False, 1+2+3 = 6, 6*3 = 18, not equal to 123', role='assistant', function_call=None, tool_calls=None))], created=1720911019, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=173, prompt_tokens=23, total_tokens=196)