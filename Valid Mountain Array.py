class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        num = -sys.maxsize
        temp = arr[-1]
        for i in range(N-2, -1, -1):
            num = max(num, temp)
            temp = arr[i]
            arr[i] = num
        arr[-1] = -1
        return arr