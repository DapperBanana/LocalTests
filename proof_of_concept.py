letion(id='chatcmpl-9fqVbEFbEYvpvfOhUUu6IQ0o64u6g', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.peek()) # Output: 2

stack.push(4)
print(stack.is_empty())  # Output: False

while not stack.is_empty():
    print(stack.pop())  # Output: 4, 2, 1

print(stack.is_empty())  # Output: True', role='assistant', function_call=None, tool_calls=None))], created=1719760319, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=193, prompt_tokens=19, total_tokens=212)