letion(id='chatcmpl-8xLZvkSQ0M53YDtRaralUrdkxYIRQ', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # Output: 1
print(q.dequeue()) # Output: 2

q.enqueue(4)
print(q.size()) # Output: 2', role='assistant', function_call=None, tool_calls=None))], created=1709154991, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_86156a94a0', usage=CompletionUsage(completion_tokens=142, prompt_tokens=19, total_tokens=161)