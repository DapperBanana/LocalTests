letion(id='chatcmpl-90vdZLQcDMkKg51t0s4udKVApJtyd', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)

# Example usage
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2

print("Size of queue:", q.size())  # Output: 1
print("Is queue empty?", q.is_empty())  # Output: False', role='assistant', function_call=None, tool_calls=None))], created=1710008585, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_2b778c6b35', usage=CompletionUsage(completion_tokens=158, prompt_tokens=19, total_tokens=177)