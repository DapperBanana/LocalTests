
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

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

    def delete_node(self, key):
        current = self.head

        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

# Create an instance of the LinkedList class
linked_list = LinkedList()

# Insert data at the beginning of the linked list
linked_list.insert_at_beginning(3)
linked_list.print_list()

# Insert data at the end of the linked list
linked_list.insert_at_end(6)
linked_list.insert_at_end(9)
linked_list.print_list()

# Delete a node from the linked list
linked_list.delete_node(6)
linked_list.print_list()
