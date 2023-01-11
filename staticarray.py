class StaticArrays:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
        self.capacity = capacity
        self.length = length
        self.arr = arr
    
    def insertEnd(self, value):
        if self.length < self.capacity:
            self.arr[self.length] = value
            self.length += 1
            return 'valid'
        
        return 'Not valid'
    
    def removeEnd(self):
        if self.length > 0:
            self.length -= 1
            return 'valid'
        return 'Not valid'

    
    def insertMiddle(self, index, value):
        if index > -1 and index < self.length:
            for i in range(self.length, index, -1):
                self.arr[i] = self.arr[i - 1]
            self.arr[index] = value
            self.length += 1
            return 'valid'
        return 'Not valid'

    
    def removeMiddle(self, index):
        if index > -1 and index < self.length:
            for i in range(index,self.length):
                self.arr[i] = self.arr[i + 1]
            self.length -= 1
            return 'valid'
        return 'Not valid'

    
    def printArr(self):
        print(self.arr[:self.length])
p = StaticArrays()
p.insertEnd(1)
p.insertEnd(4)
p.insertEnd(5)
p.printArr()
p.insertMiddle(0,7)
p.printArr()
p.removeMiddle(2)
p.printArr()


