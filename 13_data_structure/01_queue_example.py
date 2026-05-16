class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0  # Keeps track of the current number of elements

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue item.")
            return False
        
        self.queue[self.rear] = item
        # Use modular arithmetic to wrap the pointer around to the front if necessary
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue from empty queue.")
            return None
        
        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear the slot
        # Use modular arithmetic to move the front pointer forward safely
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def display(self):
        print(f"Queue State: {self.queue} | Front Pointer: {self.front} | Rear Pointer: {self.rear}")

# --- Example Usage for Live Classroom Demo ---
cq = CircularQueue(3)
cq.enqueue("A")
cq.enqueue("B")
cq.enqueue("C")
cq.display()  # Full queue

cq.dequeue()   # Removes 'A'
cq.enqueue("D") # 'D' wraps back around into the index previously held by 'A'
cq.display()
