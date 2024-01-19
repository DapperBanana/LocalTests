
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def get_front(self):
        if self.is_empty():
            return None
        return self.queue[0]


# Example usage
queue = Queue()

# Enqueue elements
queue.enqueue('apple')
queue.enqueue('banana')
queue.enqueue('cherry')

# Print queue size
print("Size:", queue.size())  # Output: 3

# Dequeue elements
print(queue.dequeue())  # Output: apple
print(queue.dequeue())  # Output: banana

# Print queue size after dequeuing
print("Size:", queue.size())  # Output: 1

# Get the front element
print("Front:", queue.get_front())  # Output: cherry
