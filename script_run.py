
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Test the Stack implementation
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3
print(stack.peek())  # 2
print(stack.size())  # 2

while not stack.is_empty():
    print(stack.pop())
