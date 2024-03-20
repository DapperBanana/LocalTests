letion(id='chatcmpl-94wNf5mAJkk7pW9BHNdMt4jfmR1Af', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def hamming_distance(str1, str2):
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
print("Hamming distance between 'karolin' and 'kathrin' is:", hamming_distance(str1, str2))

str3 = "1011101"
str4 = "1001001"
print("Hamming distance between '1011101' and '1001001' is:", hamming_distance(str3, str4))', role='assistant', function_call=None, tool_calls=None))], created=1710964755, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=160, prompt_tokens=21, total_tokens=181)