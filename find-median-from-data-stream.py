class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.right == []:
            heappush(self.right, num)
        else:
            if num > self.right[0]:
                heappush(self.right, num)
            else:
                heappush(self.left, -num)
            
            if len(self.right) > len(self.left) + 1:
                heappush(self.left, -heappop(self.right))
            
            if len(self.left) > len(self.right) + 1:
                heappush(self.right, -heappop(self.left))
        
    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return self.right[0]
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (self.right[0] - self.left[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()