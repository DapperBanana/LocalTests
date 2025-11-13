
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def delete(self, target):
        current = self.head
        if current and current.data == target:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != target:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

# Example usage
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.display()  # Output: 1 2 3
print(llist.search(3))  # Output: True
llist.delete(2)
llist.display()  # Output: 1 3
