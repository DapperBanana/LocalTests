
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Testing the stack implementation
s = Stack()
s.push(1)
s.push(2)
s.push(3)

print("Stack size:", s.size())
print("Pop item from stack:", s.pop())
print("Peek item from stack:", s.peek())
print("Is stack empty?", s.is_empty())

