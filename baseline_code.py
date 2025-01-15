
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
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
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
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# create a linked list
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)

# print the list
print("Original Linked List:")
llist.print_list()

# prepend a node
llist.prepend(0)
print("Linked List after prepending 0:")
llist.print_list()

# delete a node
llist.delete(2)
print("Linked List after deleting 2:")
llist.print_list()
