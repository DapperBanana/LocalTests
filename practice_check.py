letion(id='chatcmpl-91ggLGyMmKCkqSDd7buH7sTEtl9P4', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def hamming_distance(str1, str2):
    distance = 0
    if len(str1) != len(str2):
        raise ValueError("The two strings must be of equal length for Hamming distance calculation")
        
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
            
    return distance

# Test the function
string1 = "karolin"
string2 = "kathrin"
print(hamming_distance(string1, string2)) # Output: 3', role='assistant', function_call=None, tool_calls=None))], created=1710189425, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=112, prompt_tokens=21, total_tokens=133)