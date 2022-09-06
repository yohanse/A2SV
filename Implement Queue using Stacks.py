class MyQueue:

    def __init__(self):
        self.joo1=[]
        self.joo2=[]
        

    def push(self, x: int) -> None:
        self.joo2.append(x)
        

    def pop(self) -> int:
        if self.joo1==[]:
            while not self.joo2==[]:
                self.joo1.append(self.joo2.pop())
        return self.joo1.pop()

    def peek(self) -> int:
        if self.joo1==[]:
            while not self.joo2==[]:
                self.joo1.append(self.joo2.pop())
        return self.joo1[-1]
        

    def empty(self) -> bool:
        if self.joo1==[] and self.joo2==[]:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()