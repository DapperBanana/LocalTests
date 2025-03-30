
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", self.queue)

# Test the Queue class
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()

print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())

queue.display()
