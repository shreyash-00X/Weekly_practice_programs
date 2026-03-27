class Queue:
    def __init__(self, length):
        self.main = []
        self.length = length
        self.count = 0

    def enqueue(self, value):
        if self.length  == self.count:
            print("Overflow")
            return
        
        try:
            value = int(value)
        except Exception :
            return "Invalid input"

        # Insertion
        self.main.append(value)
        self.count += 1
        
        print("Space left: ", self.length - self.count)

    def dequeue(self):
        if self.count == 0:
            print("Underflow")
            return None
        else:
            removed = self.main.pop(0)
            self.count -= 1
            print("Space increased: ", self.length - self.count)
            print("Value removed: ", removed)

    def peek(self):
        if self.count == 0:
            return "Empty queue"
        return self.main[0]

        
queue = Queue(2)
queue.enqueue(1)
queue.enqueue(2)
