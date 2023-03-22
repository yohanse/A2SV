class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        arr = [0] * n
        res = [0]
        N = len(requests)

        def backtrack(arr, index, count):
            if index == N:
                if max(arr) == min(arr) == 0:
                    res[0] = max(res[0], count)
                return
        
            start, end = requests[index]
            backtrack(arr, index + 1, count)
         
            arr[start] -= 1
            arr[end] += 1 
            backtrack(arr, index + 1, count + 1)
            arr[start] += 1
            arr[end] -= 1

        backtrack(arr, 0, 0)
        return res[0]