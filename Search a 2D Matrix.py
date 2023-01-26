class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        def search():

            l, r = 0, n - 1

            while l < r:

                mid = (l + r + 1)//2

                if matrix[mid][0] <= target:
                    l = mid

                else:
                    r = mid - 1

            return l
        
        def searchf(i):

            l, r = 0, m

            while l < r:
                
                mid = (l + r)//2
                

                if matrix[i][mid] == target:
                    return True

                elif target > matrix[i][mid]:
                    l = mid + 1

                else:
                    r = mid

            return False

        
        return searchf(search())