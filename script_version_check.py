
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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

# Create a linked list
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

# Display the linked list
print("Linked List:")
llist.display()

# Delete a node
llist.delete(3)

# Display the linked list after deletion
print("\nLinked List after deleting 3:")
llist.display()
