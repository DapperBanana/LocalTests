letion(id='chatcmpl-9LG3zY0I5lyVquoSHnbV7Voq5b9k8', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

sentence = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(sentence)
print("Reversed sentence: ", reversed_sentence)', role='assistant', function_call=None, tool_calls=None))], created=1714853663, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3b956da36b', usage=CompletionUsage(completion_tokens=54, prompt_tokens=21, total_tokens=75)