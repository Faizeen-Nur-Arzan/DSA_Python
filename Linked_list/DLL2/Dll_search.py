class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
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
        new_node.prev = last

    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        
        current = self.head
        print("None ⇆ ", end = "")
        
        while current:
            print(current.data, end = "⇆")
            current = current.next
        print("None")
    
    def search(self, key):
        current = self.head
        position = 0

        while current:
            if current.data == key:
                return current, position
            current = current.next
            position += 1
        
        return None, -1

if __name__ == "__main__":
    dll = DoublyLinkedList()
    for value in [10, 20, 30, 40, 50, 60]:
        dll.append(value)
    
    print("Original doubly Linked List:")
    dll.display()

    print("\n*** -SEARCHING- ***")
    node, pos = dll.search(40)
    if node:
        print(f"40 found at position {pos}")
    else:
        print("40 not found")