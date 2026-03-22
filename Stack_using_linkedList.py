class Node:
    def  __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None        #Reference var | stores latest node's address


    def in_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    


class Stack:

    def __init__(self, size):
        self.size = size
        self.count = 0
        self.space = 0
        self.ll = LinkedList()
        
    def push(self, value):
        if self.count == self.size:
            print("Overflow")
        else:
            self.ll.in_beg(value)
            self.count += 1
            self.space = self.size - self.count
            print(f"Space left: {self.space}")
           # print(self.ll.head.data)       #       Value

    def pop(self):
        if self.count == 0:
            print("Underflow")
        else:
            latest_value = self.ll.head.data
            self.ll.head = self.ll.head.next
            self.count -= 1
            self.space += 1
            print(f"Space increase to: {self.space}")
            print(f"item popped: {latest_value}")
            

    def peek(self):
        if self.ll.head is not None:
            print(self.ll.head.data)
        return None
