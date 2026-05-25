class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push1(self, value):
        self.stack1.append(value)
    
    def pop1(self):
        if len(self.stack1) != 0:
            self.stack1.pop()
    
    def is_empty1():
        if len(self.stack1) == 0:
            return True
        return False
    
    def push2(self, value):
        self.stack2.append(value)
    
    def pop2(self):
        if len(self.stack2) != 0:
            self.stack2.pop()
    
    def is_empty2():
        if len(self.stack2) == 0:
            return True
        return False

koala = Stack()