class Node:
    def __init__(self, dta):
        self.data = dta
        self.next = None

class Quelala:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return (self.front == None)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        print(f"=== DATA-ENQUEUED-SUCCESFULLY ===\nData added:\n{value}")