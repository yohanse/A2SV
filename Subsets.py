class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans1,N=[],len(nums)
        def back(n,N,j=0,ans=[]):
            if N==j:
                ans1.append(ans)
                return
            back(n,N,j+1,ans)
            back(n,N,j+1,ans+n[j:j+1])
        back(nums,N)
        return ans1