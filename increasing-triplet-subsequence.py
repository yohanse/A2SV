class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        left = [sys.maxsize for i in range(n)]
        mini = nums[0] 
        for i in range(n):
            mini = min(nums[i], mini)
            left[i] = mini
        maxi = nums[-1]
        for i in range(n - 2, 0, -1):
            if left[i] < nums[i] < maxi:
                return True
            maxi = max(maxi, nums[i])

        return False