letion(id='chatcmpl-9djJsbPSCxXTXa8xJBmRpwcs0qKtx', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_num = ""
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num = decimal_num // 2
    
    return binary_num

decimal_num = int(input("Enter a decimal number: "))
binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is: {binary_num}")', role='assistant', function_call=None, tool_calls=None))], created=1719256028, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=101, prompt_tokens=19, total_tokens=120)