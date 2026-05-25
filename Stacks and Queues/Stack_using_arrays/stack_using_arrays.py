class Stack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.stack = []           # Internal list acting as the array
        self.top = -1             # -1 means the stack is empty
    
    # Push an element onto the stack
    def push(self, value):
        if self.is_full():
            print("Stack Overflow! Cannot push", value)
            return
        self.stack.append(value)
        self.top += 1
        print(f"Pushed: {value}")
    
    # Remove the top element off the stack
    def remove(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
            return None
        value = self.stack.pop()
        self.top -= 1
        return value
    
    # Peek at the top element without removing it
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[self.top]
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1
    
    def size(self):
        return self.top + 1
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top → bottom):", self.stack[::-1])

s = Stack(capacity=5)
s.display()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.display()

s.push(60)

print("Peek:", s.peek())
print("Removed:", s.remove())
print("Size after remove:", s.size())
s.display()

print("Removed:", s.remove())
print("Size after remove:", s.size())
s.display()