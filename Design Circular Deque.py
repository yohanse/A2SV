class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.front = -1
        self.last = -1
        self.size = 0
        self.list = [-1]*k
        

    def insertFront(self, value: int) -> bool:
        if self.size != self.capacity:
            if self.size == 0:
                self.list[0] = value
                self.front = 0
                self.last = 0
            else:
                if self.front == 0:
                    self.front = self.capacity
                self.list[self.front - 1] = value
                self.front -= 1
            self.size += 1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if self.size != self.capacity:
            if self.size == 0:
                self.list[0] = value
                self.front = 0
                self.last = 0
            else:
                self.last = (self.last + 1) % self.capacity
                self.list[self.last] = value
            self.size += 1
            return True
        return False
        

    def deleteFront(self) -> bool:
        if self.size:
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size:
            self.last = self.last - 1
            if self.last < 0:
                self.last += self.capacity
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.size:
            return self.list[self.front]
        return -1

    def getRear(self) -> int:
        if self.size:
            return self.list[self.last]
        return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()