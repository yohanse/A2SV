class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N,target,dp=len(nums),sum(nums),{}
        if target%2:return False
        target=target//2
        def dynamic(pos,target):
            if pos==N:return False
            elif target<0:return False
            elif target==0:return True
            elif (pos,target) in dp:return dp[(pos,target)]
            dp[(pos,target)]=dynamic(pos+1,target) or dynamic(pos+1,target-nums[pos])
            return dp[(pos,target)]
        return dynamic(0,target)