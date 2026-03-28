class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value, priority):
        new_node = Node(value, priority)

        if self.head is None or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        while temp.next and temp.next.priority >= priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def dequeue(self):
        if self.head is None:
            print("Underflow")
            return

        removed = self.head.data
        self.head = self.head.next

        print("Removed:", removed)

    def peek(self):
        if self.head is None:
            print("Empty queue")
        else:
            print("Front:", self.head.data)


pq = PriorityQueue()

pq.enqueue(10,1)
pq.enqueue(20,3)
pq.enqueue(15,2)

pq.peek()
pq.dequeue()
