
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Example usage:
stack = Stack()

stack.push(5)
stack.push(3)
stack.push(8)

print("Size of stack:", stack.size())
print("Top element:", stack.peek())

print("Pop element:", stack.pop())

print("Is the stack empty?", stack.is_empty())
