
class Node:
    def __init__(self, data):
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
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            return
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

# Example usage
ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)

print("Original List:")
ll.print_list()

ll.delete(2)

print("\nList after deleting 2:")
ll.print_list()
