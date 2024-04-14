letion(id='chatcmpl-9DyTshwhYqHwFm8j4fqeBcUwULyIm', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

def generate_markov_text(text, chain_length=2, num_words=20):
    words = text.split()
    chains = {}
    for i in range(len(words) - chain_length):
        key = tuple(words[i:i+chain_length])
        value = words[i+chain_length]
        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]
    
    key = random.choice(list(chains.keys()))
    gen_text = list(key)
    
    while len(gen_text) < num_words:
        if key in chains:
            next_word = random.choice(chains[key])
            gen_text.append(next_word)
            key = tuple(gen_text[-chain_length:])
        else:
            break
    
    return ' '.join(gen_text)

text = "I like to eat apples and bananas. I like to go for a walk in the park. I also like to read books on the weekends."

generated_text = generate_markov_text(text)
print(generated_text)', role='assistant', function_call=None, tool_calls=None))], created=1713117780, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_c2295e73ad', usage=CompletionUsage(completion_tokens=208, prompt_tokens=21, total_tokens=229)