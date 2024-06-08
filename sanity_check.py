letion(id='chatcmpl-9XvYkozoJqdt4DfZoZBWM5YEtdfdA', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

# Test the function
str1 = "karolin"
str2 = "kathrin"
print("Hamming distance between 'karolin' and 'kathrin':", hamming_distance(str1, str2))

str1 = "karolin"
str2 = "kerstin"
print("Hamming distance between 'karolin' and 'kerstin':", hamming_distance(str1, str2))', role='assistant', function_call=None, tool_calls=None))], created=1717873110, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=154, prompt_tokens=21, total_tokens=175)