class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        #to make array increase by 2 to handle edge case
        matrix = [[0 for i in range(n + 2)] for j in range(n + 2)]
        for top_row, top_col, bottom_row, bottom_col in queries:
            matrix[top_row + 1][top_col + 1] += 1
            matrix[bottom_row + 2][bottom_col + 2] += 1
            matrix[top_row + 1][bottom_col + 2] -= 1
            matrix[bottom_row + 2][top_col + 1] -= 1
        
        #make the prefix sum
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] -  matrix[i - 1][j - 1]

        #copy the array by decreasing by two size increase before
        res = [[0 for i in range(n)] for j in range(n)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                res[i - 1][j - 1] = matrix[i][j]

        return res 