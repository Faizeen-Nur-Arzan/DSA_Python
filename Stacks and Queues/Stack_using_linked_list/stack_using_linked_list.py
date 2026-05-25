#Stack Implementation Using Liked List (Python)
class Node:
    def __init__(self, data):
        self.data = data   # The value stored in this node
        self.next = None   # Pointer to the node below it

class StackLL:
    def __init__(self):
        self.top = None    # Points to the top node
        self._size = 0
    
    # Push: create a new node, point it to current top, update top
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top    # New node points to old top
        self.top = new_node         # Update top to new_node
        self._size += 1
        print(f"Pushed: {value}")
    
    # Pop: save top's value, move top to next node
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
            return None
        popped_val = self.top.data
        self.top = self.top.next       # Move top pointer down
        self._size -= 1
        return popped_val