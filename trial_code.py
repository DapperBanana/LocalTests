letion(id='chatcmpl-8eDf0zNajHXSk4hIvXH1Apv4bm0ss', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def generate_fibonacci(n):
    sequence = [0, 1]  # Initialize the sequence with the first two terms

    for i in range(2, n):
        # Calculate the next term by summing the previous two terms
        next_term = sequence[i - 1] + sequence[i - 2]
        
        # Add the next term to the sequence
        sequence.append(next_term)

    return sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms to generate: "))

# Generate and print the Fibonacci sequence
fib_sequence = generate_fibonacci(num_terms)
print("Fibonacci Sequence:")
for term in fib_sequence:
    print(term)', role='assistant', function_call=None, tool_calls=None))], created=1704596322, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=150, prompt_tokens=24, total_tokens=174)