letion(id='chatcmpl-96nUjVVRGnJm0rmpVXl72ddWkFAQX', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to convert string to title case 
def convert_to_titlecase(s):
    return s.title()

# Take user input
string = input("Enter a string: ")

# Convert string to title case
title_string = convert_to_titlecase(string)

# Display the title case string
print("Title case string:", title_string)', role='assistant', function_call=None, tool_calls=None))], created=1711407253, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=67, prompt_tokens=19, total_tokens=86)