class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = n = len(nums)
        nums = list(set(nums))
        nums.sort()
        queue = deque()
        for num in nums:
            if queue and queue[0] < num - n + 1:
                queue.popleft()
            queue.append(num)
            ans = min(ans, n - len(queue))
        return ans