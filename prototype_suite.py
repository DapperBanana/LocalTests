letion(id='chatcmpl-9AR6GXzyYC9glMFt3LxyVayOjt39D', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def reverse_words(sentence):
    words_list = sentence.split()
    reversed_sentence = ' '.join(reversed(words_list))
    return reversed_sentence

# Test the function
sentence = "Hello World!"
result = reverse_words(sentence)
print(result) # Output: "World! Hello"', role='assistant', function_call=None, tool_calls=None))], created=1712274480, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_b28b39ffa8', usage=CompletionUsage(completion_tokens=57, prompt_tokens=21, total_tokens=78)