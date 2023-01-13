class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length_row = len(matrix)
        length_col = len(matrix[0])

        for row in range(length_row):
            for col in range(length_col):
                if matrix[row][col]==0:
                    
                    for j in range(length_col):
                        if matrix[row][j]!=0:
                            matrix[row][j]="a"

                    for i in range(length_row):
                        if matrix[i][col]!=0:
                            matrix[i][col]="a"
        
        for row in range(length_row):
            for col in range(length_col):
                if matrix[row][col]=="a":
                    matrix[row][col]=0