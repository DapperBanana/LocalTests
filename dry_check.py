letion(id='chatcmpl-9buQEYIDIcp1PrMY9snYsMyJuIISW', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='class Stack:
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

    def size(self):
        return len(self.stack)

# Example Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop()) # Stack is empty message will be printed', role='assistant', function_call=None, tool_calls=None))], created=1718822050, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=163, prompt_tokens=19, total_tokens=182)