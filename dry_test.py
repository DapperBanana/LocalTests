
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Create a linked list
llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)

# Print the linked list
print("Linked list:")
llist.print_list()

# Delete a node from the linked list
llist.delete(2)

# Print the linked list after deletion
print("Linked list after deleting node with data 2:")
llist.print_list()
