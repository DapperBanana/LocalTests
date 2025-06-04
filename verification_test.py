
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

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

# Test the linked list operations
linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Linked list elements:")
linked_list.display()
print()

print("Search element 2 in linked list:")
print(linked_list.search(2))

print("Search element 4 in linked list:")
print(linked_list.search(4))

print("Delete element 2 from linked list:")
linked_list.delete(2)

print("Linked list after deletion:")
linked_list.display()
