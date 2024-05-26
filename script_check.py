letion(id='chatcmpl-9TCsdJe0pdunDpKBI50P7NnkTIras', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

# Test the stack implementation
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3
print(stack.pop())   # Output: 2
print(stack.peek())  # Output: 1
print(stack.pop())   # Output: 1
print(stack.pop())   # Output: Stack is empty', role='assistant', function_call=None, tool_calls=None))], created=1716748051, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=192, prompt_tokens=19, total_tokens=211)