letion(id='chatcmpl-9bBmCUGBpC9l2L9gv3dHOPlZcEQIf', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random
import string

def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

length = int(input("Enter the length of the password: "))
print("Generated Password:", generate_password(length))', role='assistant', function_call=None, tool_calls=None))], created=1718650432, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=65, prompt_tokens=21, total_tokens=86)