class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item, priority):
        """
        Inserts an item with an integer priority value.
        Lower numerical value = Higher real-world priority (e.g., Priority 1 goes first).
        """
        new_element = {"data": item, "priority": priority}
        
        # If queue is empty, just append
        if self.is_empty():
            self.queue.append(new_element)
            return

        # Find the correct spot to insert the item to keep the queue sorted
        inserted = False
        for i in range(len(self.queue)):
            if new_element["priority"] < self.queue[i]["priority"]:
                self.queue.insert(i, new_element)
                inserted = True
                break
        
        if not inserted:
            self.queue.append(new_element)

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Priority Queue is empty.")
            return None
        # Since it's kept sorted, the front of the list is always highest priority
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def display(self):
        for index, item in enumerate(self.queue):
            print(f"[{index}] Data: {item['data']}, Priority: {item['priority']}")

# --- Example Usage for Live Classroom Demo ---
pq = PriorityQueue()
pq.enqueue("Routine Task A", priority=3)
pq.enqueue("Emergency Critical Task B", priority=1)
pq.enqueue("Moderate Task C", priority=2)

print("Priority Queue State (Sorted automatically upon insertion):")
pq.display()

print(f"\nProcessing first item: {pq.dequeue()}") # Processed "Emergency Critical Task B" first
