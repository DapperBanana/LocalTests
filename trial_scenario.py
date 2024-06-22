letion(id='chatcmpl-9czz0jwR8IlAniATz30uefCiN1JPj', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Implementing a simple stack data structure in Python

class Stack:
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

# Testing the stack implementation
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Stack peek:", stack.peek())

print("Pop item from stack:", stack.pop())
print("Pop item from stack:", stack.pop())
print("Pop item from stack:", stack.pop())

print("Is stack empty?", stack.is_empty())', role='assistant', function_call=None, tool_calls=None))], created=1719081754, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=204, prompt_tokens=19, total_tokens=223)