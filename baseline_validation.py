letion(id='chatcmpl-96nVldlIn82taR0UciyFn6ciGYONW', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

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

# Testing the Stack implementation
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Current stack:")
print(stack.stack)

print("Popped element:", stack.pop())
print("Stack after pop:")
print(stack.stack)

print("Peek element:", stack.peek())', role='assistant', function_call=None, tool_calls=None))], created=1711407317, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=163, prompt_tokens=19, total_tokens=182)