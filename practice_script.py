
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
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head
        if current is not None:
            if current.data == key:
                self.head = current.next
                current = None
                return
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next
        if current == None:
            return
        prev.next = current.next
        current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Create a linked list
llist = LinkedList()
llist.insert_at_beginning(3)
llist.insert_at_end(6)
llist.insert_at_end(9)
llist.insert_at_end(12)

# Print the linked list
print("Linked List:")
llist.print_list()

# Insert an element at a specific position
llist.insert_at_position(2, 7)
print("Linked List after inserting 7 at position 2:")
llist.print_list()

# Delete an element from the linked list
llist.delete_node(6)
print("Linked List after deleting 6:")
llist.print_list()
