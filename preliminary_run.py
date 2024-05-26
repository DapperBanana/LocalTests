letion(id='chatcmpl-9TCmgDLX613BO3tSn1d8PzgU8PKUn', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(input_string))', role='assistant', function_call=None, tool_calls=None))], created=1716747682, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=71, prompt_tokens=22, total_tokens=93)