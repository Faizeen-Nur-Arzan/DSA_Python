class Node:
    def __init__(self, dta):
        self.data = dta
        self.next = None

class Quelala:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size =0
    
    def is_empty(self):
        return (self.front == None)
    
    def size(self):
        return self._size
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size +=1
        print(f"=== DATA-ENQUEUED-SUCCESFULLY ===\nData enqueued:\n{value}")
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("=== EMPTY-QUEUE-ERROR ===\nCouldn't delete from empty list.")
            return None
        print(f"=== DATA-DEQUEUED-SUCCESSFULLY ===\nData dequeued:\n{self.front}")
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        
        self._size -=1
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty - nothing to peek at.")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Queue [FRONT → REAR]:", " → ". join(elements))

if __name__ == "__main__":
    q = Quelala()
    q.display()

    q.enqueue("Player_Alpha")
    q.enqueue("Player_Beta")
    q.enqueue("Player_Gamma")
    q.enqueue("PLayer_Delta")

    q.display()
    print(f"Queue size : {q.size()}")
    print(f"Front item : {q.peek()}")

    print("\n--- Processing Respawn Queue ---")
    q.dequeue()
    q.dequeue()
    q.display()

    print(f"\nIs queue empty? {q.is_empty()}")
    q.dequeue()
    q.dequeue()
    q.dequeue()