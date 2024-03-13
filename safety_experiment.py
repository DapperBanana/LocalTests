letion(id='chatcmpl-927HLDu2v6LxztGPKSNYt13L7hWzD', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

# Example Usage

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Top element:", stack.peek())

print("Popping elements:")
while not stack.is_empty():
    print(stack.pop())

print("Stack size:", stack.size())', role='assistant', function_call=None, tool_calls=None))], created=1710291663, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=170, prompt_tokens=19, total_tokens=189)