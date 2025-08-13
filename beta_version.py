
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)

# Create a new queue
q = Queue()

# Enqueue elements
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Display queue
q.display()

# Dequeue elements
print(q.dequeue())
print(q.dequeue())

# Display queue after dequeue
q.display()
