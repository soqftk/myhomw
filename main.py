class Node:
    def __init__(self, next_node, prev_node, data) -> None:
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None 

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node 
        else:
            current = self.head 
            while current.next_node:
                current = current.next_node 
            current.next_node = new_node 
            new_node.prev_node = current 

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node

    def print_list(self):
        if self.is_empty():
            print("Doubly linked list is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next_node
        print()


a = DoublyLinkedList()

a.append(1)
a.append(2)
a.append(3)
a.prepend(4)

print(a)
