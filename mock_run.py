
class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print("Queue:", self.items)


queue = Queue()
queue.enqueue(1)
queue.display()  # Output: Queue: [1]
queue.enqueue(2)
queue.display()  # Output: Queue: [1, 2]
queue.enqueue(3)
queue.display()  # Output: Queue: [1, 2, 3]
queue.dequeue()
queue.display()  # Output: Queue: [2, 3]
print("Size:", queue.size())  # Output: Size: 2
