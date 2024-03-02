letion(id='chatcmpl-8yS2yyw5EjQDwoSfHrYWZYNORcmuZ', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to check if the given matrix is a magic torus
def is_magic_torus(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])

    # Check rows sum
    for i in range(n):
        if sum(matrix[i]) != magic_sum:
            return False

    # Check columns sum
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False

    # Check main diagonal sum
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False

    # Check secondary diagonal sum
    if sum(matrix[i][n-1-i] for i in range(n)) != magic_sum:
        return False

    return True

# Test the function with an example matrix
matrix = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

if is_magic_torus(matrix):
    print("The given matrix is a magic torus.")
else:
    print("The given matrix is not a magic torus.")', role='assistant', function_call=None, tool_calls=None))], created=1709418184, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_2b778c6b35', usage=CompletionUsage(completion_tokens=235, prompt_tokens=23, total_tokens=258)