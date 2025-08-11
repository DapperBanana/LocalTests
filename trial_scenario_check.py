
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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                new_node.next = current.next
                current.next = new_node
                break
            count += 1
            current = current.next
        if current is None:
            print("Index out of bounds.")

    def delete_at_index(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                current.next = current.next.next
                break
            count += 1
            current = current.next
        if current is None:
            print("Index out of bounds.")

# Create a linked list
llist = LinkedList()

# Append data to the linked list
llist.append(1)
llist.append(2)
llist.append(3)

# Display the linked list
print("Linked list: ")
llist.display()
print()

# Insert data at index
llist.insert_at_index(1, 5)

# Display the linked list after insertion
print("Linked list after insertion: ")
llist.display()
print()

# Delete data at index
llist.delete_at_index(1)

# Display the linked list after deletion
print("Linked list after deletion: ")
llist.display()
