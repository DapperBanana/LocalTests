letion(id='chatcmpl-9DHN5mgFyr8eLRJK4DX9IEQ9nlYWb', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="import re

def extract_emails_from_text(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

text = '''
Hello, my email is john.doe@example.com. Please contact me at jane.smith@email.com for further information.
'''

emails = extract_emails_from_text(text)

print(emails)", role='assistant', function_call=None, tool_calls=None))], created=1712952067, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_c2295e73ad', usage=CompletionUsage(completion_tokens=102, prompt_tokens=21, total_tokens=123)