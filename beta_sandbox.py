letion(id='chatcmpl-8ulauj3vEUrCk2vdMc3qkdZKcEFj6', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1
print(stack.pop())  # Output: None', role='assistant', function_call=None, tool_calls=None))], created=1708540012, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_cbdb91ce3f', usage=CompletionUsage(completion_tokens=163, prompt_tokens=19, total_tokens=182)