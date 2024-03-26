letion(id='chatcmpl-97AR1hHZlzAu5BUhcJIYGKvXcmdTE', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

sentence = "Hello world how are you"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)', role='assistant', function_call=None, tool_calls=None))], created=1711495435, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=49, prompt_tokens=21, total_tokens=70)