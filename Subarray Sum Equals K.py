class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        perfixsum={0:1}
        tot=0
        ans=0
        for value in nums:
            tot=tot+value
            target=tot-k
            ans=ans+perfixsum.get(target,0)
            perfixsum[tot]=perfixsum.get(tot,0)+1
        return ans