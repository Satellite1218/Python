class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.deque = [None] * capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def addFront(self, data):
        if self.isFull():
            print("Deque is full")
            return
        self.front = (self.front - 1) % self.capacity
        self.deque[self.front] = data
        self.size += 1

    def addRear(self, data):
        if self.isFull():
            print("Deque is full")
            return
        self.deque[self.rear] = data
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def removeFront(self):
        if self.isEmpty():
            print("Deque is empty")
            return None
        data = self.deque[self.front]
        self.deque[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data

    def removeRear(self):
        if self.isEmpty():
            print("Deque is empty")
            return None
        self.rear = (self.rear - 1) % self.capacity
        data = self.deque[self.rear]
        self.deque[self.rear] = None
        self.size -= 1
        return data

    def getFront(self):
        if self.isEmpty():
            print("Deque is empty")
            return None
        return self.deque[self.front]

    def getRear(self):
        if self.isEmpty():
            print("Deque is empty")
            return None
        return self.deque[(self.rear - 1) % self.capacity]
