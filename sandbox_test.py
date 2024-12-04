
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
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def delete(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

# Creating a linked list
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Displaying the linked list
print("Linked List:")
linked_list.display()

# Searching for a value
print("Search for 2:", linked_list.search(2))
print("Search for 4:", linked_list.search(4))

# Deleting a value
linked_list.delete(2)
print("Linked List after deleting 2:")
linked_list.display()
