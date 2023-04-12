class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N, res = len(nums), []
        def permutation(seen, ans):
            if len(ans) == N:
                res.append(ans.copy())
                return
            
            for i in range(N):
                if not ((seen >> i) & 1):
                    seen = (1 << i) | seen
                    ans.append(nums[i])
                    permutation(seen, ans)
                    ans.pop()
                    seen = (~(1 << i)) & seen
            
        permutation(0, [])
        return res