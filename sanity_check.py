letion(id='chatcmpl-9V0lEwNW8qK0fSAyX7fERwotdEeYo', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(sentence)
print("Reversed sentence: " + reversed_sentence)', role='assistant', function_call=None, tool_calls=None))], created=1717178120, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=55, prompt_tokens=21, total_tokens=76)