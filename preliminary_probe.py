
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

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

    def delete_node(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            print(f"{data} not found in the list")
            return

        prev.next = current_node.next
        current_node = None

    def reverse_list(self):
        prev = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head = prev

# Example usage
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("Original Linked List:")
llist.print_list()

llist.delete_node(3)
print("Linked List after deleting node with value 3:")
llist.print_list()

llist.reverse_list()
print("Reversed Linked List:")
llist.print_list()
