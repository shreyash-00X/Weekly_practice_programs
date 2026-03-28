class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        if self.count == self.size:
            print("Overflow")
            return

        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1
        print("Space left:", self.size - self.count)

    def dequeue(self):
        if self.count == 0:
            print("Underflow")
            return

        removed = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.count -= 1
        print("Removed:", removed)

    def peek(self):
        if self.head is None:
            print("Empty queue")
        else:
            print(self.head.data)


queue = Queue(3)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.dequeue()
queue.peek()
