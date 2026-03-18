class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class BoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        print("None", end = " ↔ ")
        while current:
            print(current.data, end = " ↔ ")
            current = current.next
        print("None")
    
    def display_reverse(self):
        if self.tail is None:
            print("List is empty")
            return
        
        current = self.tail
        print("None", end = " ↔ ")
        while current:
            print(current.data, end = " ↔ ")
            current = current.prev
        print("None")
    
    def insert_at_beginning(self, data)