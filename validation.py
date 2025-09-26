
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Queue is empty"

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue: ", self.items)


# Test the Queue data structure
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()  # Queue:  [3, 2, 1]

print("Dequeued item:", queue.dequeue())  # Dequeued item: 1

queue.display()  # Queue:  [3, 2]
