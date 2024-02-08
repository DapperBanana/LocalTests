
# Node class to represent a single node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a new node at the beginning of the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Method to insert a new node after the given prev_node
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in the linked list.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Method to append a new node at the end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Method to delete a node with the given key
    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    # Method to print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Usage example
linked_list = LinkedList()

linked_list.push(1)
linked_list.append(2)
linked_list.append(3)
linked_list.insert_after(linked_list.head.next, 4)

print("Initial linked list:")
linked_list.print_list()

linked_list.delete_node(3)

print("Linked list after deleting node with key 3:")
linked_list.print_list()
