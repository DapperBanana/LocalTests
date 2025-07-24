
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"
    
    def size(self):
        return len(self.items)

# Example Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top element of the stack:", stack.peek())

print("Popping elements from the stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
