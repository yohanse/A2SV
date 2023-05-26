class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr) - 2
        x = n + 1
        for i in range(n, -1, -1):
            if arr[i] > arr[i + 1]:
                x = i + 1
                for j in range(i + 1, n + 2):
                    if arr[j] < arr[i] and arr[j] > arr[x]:
                        x = j
                arr[i], arr[x] = arr[x], arr[i]
                return arr
        return arr