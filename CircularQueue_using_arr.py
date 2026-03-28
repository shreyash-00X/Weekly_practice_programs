class CircularQueue:
    def __init__(self, length):
        self.main = [None] * length
        self.length = length
        self.count = 0
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if self.count == self.length:
            print("Overflow")
            return

        try:
            value = int(value)
        except Exception:
            print("Invalid input")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.length
        self.main[self.rear] = value
        self.count += 1

        print("Space left:", self.length - self.count)

    def dequeue(self):
        if self.count == 0:
            print("Underflow")
            return

        removed = self.main[self.front]
        self.main[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.length

        self.count -= 1

        print("Value removed:", removed)
        print("Space increased:", self.length - self.count)

    def peek(self):
        if self.count == 0:
            print("Empty queue")
        else:
            print(self.main[self.front])


queue = CircularQueue(3)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.dequeue()
queue.enqueue(40)

queue.peek()
