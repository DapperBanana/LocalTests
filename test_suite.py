
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
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print()

    def delete(self, key):
        curr_node = self.head
        if curr_node is not None and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev = None
        while curr_node is not None and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev.next = curr_node.next
        curr_node = None

# Main Program
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.display()

llist.delete(2)
llist.display()
