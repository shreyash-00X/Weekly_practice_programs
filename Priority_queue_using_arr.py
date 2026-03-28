class PriorityQueue:
    def __init__(self, size):
        self.main = []
        self.size = size
        self.count = 0

    def enqueue(self, value, priority):
        if self.count == self.size:
            print("Overflow")
            return

        item = (priority, value)
        self.main.append(item)
        self.count += 1

        print("Inserted:", value, "Priority:", priority)

    def dequeue(self):
        if self.count == 0:
            print("Underflow")
            return

        highest = 0
        for i in range(1, self.count):
            if self.main[i][0] > self.main[highest][0]:
                highest = i

        removed = self.main.pop(highest)
        self.count -= 1

        print("Removed:", removed[1])

    def peek(self):
        if self.count == 0:
            print("Empty queue")
            return

        highest = 0
        for i in range(1, self.count):
            if self.main[i][0] > self.main[highest][0]:
                highest = i

        print("Front:", self.main[highest][1])


pq = PriorityQueue(5)

pq.enqueue(10,1)
pq.enqueue(20,3)
pq.enqueue(15,2)

pq.peek()
pq.dequeue()
