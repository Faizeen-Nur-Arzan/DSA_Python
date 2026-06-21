class Queue:
    """
    A Queue data structure implemented using a Python. 
    Follows FIFO: First In, First Out.
    Enqueue: Always add an item from the rear end (back end). You cannot remove any item from the back in queue.
    Dequeue: Always remove an itm from the front end. You cannot add any item from the front end.
    """

    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Noting to Dequeue from an empty queue!")
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Nothing to Peek at an empty queue!")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("[ EMPTY QUEUE ]")
        else:
            print(f"FRONT => {self.items} <= REAR")
    
    def __str__(self):
        return f"Queue({self.items})"

enemy_spawn_queue = Queue()

print("=== Queuing up enemies ===")
enemy_spawn_queue.enqueue("Goblin")
enemy_spawn_queue.enqueue("Orc")
enemy_spawn_queue.enqueue("Troll")
enemy_spawn_queue.enqueue("Dragon Boss")
enemy_spawn_queue.display()

print(f"\nTotal enemies queued: {enemy_spawn_queue.size()}")
print(f"Next to spawn: {enemy_spawn_queue.peek()}")

print("\n=== Spawning enemies ===")
while not enemy_spawn_queue.is_empty():
    enemy = enemy_spawn_queue.dequeue()
    print(f"SPAWNED: {enemy}!")
    enemy_spawn_queue.display()

print("\n=== All enemies have spawned! ===")