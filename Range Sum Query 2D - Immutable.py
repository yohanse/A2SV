class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows,columns=len(matrix),len(matrix[0])
        self.sum=[[0 for i in range(columns+1)] for j in range(rows+1)]
        for i in range(rows):
            tot=0
            for j in range(columns):
                tot=tot+matrix[i][j]
                self.sum[i+1][j+1]=tot+self.sum[i][j+1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=self.sum[row2+1][col2+1]-self.sum[row1][col2+1]-self.sum[row2+1][col1]
        ans=ans+self.sum[row1][col1]
        return ans
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)