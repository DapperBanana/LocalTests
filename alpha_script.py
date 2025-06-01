
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Create a linked list
llist = LinkedList()

# Insert elements
llist.insert_at_beginning(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.insert_at_end(4)

# Display the linked list
print("Linked list:")
llist.display()

# Delete an element
llist.delete(3)

# Display the linked list after deletion
print("Linked list after deletion:")
llist.display()
