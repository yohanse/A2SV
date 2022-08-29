class MinStack:

    def __init__(self):
        self.minimum=[]
        self.last=-1
        self.joo=[]
        

    def push(self, val: int) -> None:
        self.last=self.last+1
        self.joo.append(val)
        

    def pop(self) -> None:
        self.last=self.last-1
        self.joo.pop()
        
        

    def top(self) -> int:
        return self.joo[self.last]
        

    def getMin(self) -> int:
        minimum=self.joo[0]
        for i in self.joo:
            if i<minimum:
                minimum=i
        return minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()