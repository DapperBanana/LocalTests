letion(id='chatcmpl-9S7zCmcHJX7gOtA4DiCre8OJDkuTf', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Implementing a simple stack data structure in Python

class Stack:
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
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top element of stack:", stack.peek())
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())
print("Is stack empty?", stack.is_empty())', role='assistant', function_call=None, tool_calls=None))], created=1716490910, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=176, prompt_tokens=19, total_tokens=195)