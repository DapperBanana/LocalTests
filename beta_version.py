letion(id='chatcmpl-9hiGCDeeLOOF3QLewdA8Dah2oo1yU', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to count occurrences of each character in a string
def count_characters(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

# Main program
string = input("Enter a string: ")
char_count = count_characters(string)

print("\nCharacter Counts:")
for char, count in char_count.items():
    print(char, ":", count)', role='assistant', function_call=None, tool_calls=None))], created=1720205268, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=105, prompt_tokens=24, total_tokens=129)