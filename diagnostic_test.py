letion(id='chatcmpl-9XFFD2shsHVIzw52dQpmtoRg4JGT9', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def count_vowels(text):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
            
    return vowel_count

input_text = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(input_text))', role='assistant', function_call=None, tool_calls=None))], created=1717710451, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=74, prompt_tokens=22, total_tokens=96)