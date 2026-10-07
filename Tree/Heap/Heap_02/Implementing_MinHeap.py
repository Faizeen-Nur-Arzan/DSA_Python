class MinHeap:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def peek(self):
        if not self.data:
            raise IndexError("Heap is empty. Nothing to see.")
        return self.data[0]
    
    def push(self, value):
        self.data.append(value)   # 1) Add at the next open leaf.
        self._shift_up(len(self.data) - 1)   # 2) Bubble it up into place.
    
    def _shift_up(self, i):
        while i > 0:
            parent = (i-1) // 2
            if self.data[i] < self.data[parent]:   # Child smaller than parent? Swap.
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break   # Heap property satisfied, stop.
    
    def __repr__(self):
        return f"MinHeap({self.data})"

h = MinHeap()
for value in [90, 70, 50, 80, 10, 20, 30, 60, 40]:
    h.push(value)
    print(f"push({value:2}) -> {h}")

print("\npeek():", h.peek())