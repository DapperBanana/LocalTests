
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

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

# Create a linked list
llist = LinkedList()

llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_end(15)
llist.insert_at_end(20)

print("Linked list:")
llist.display()

llist.delete_node(10)
print("Linked list after deleting 10:")
llist.display()
