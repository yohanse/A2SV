class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = [[] for _ in range(N)]
        temp1 = []
        for i in range(N):
            for j in range(i):
                if nums[i] >= nums[j]:
                    for _ in res[j]:
                        temp = _.copy()
                        temp.append(nums[i])
                        res[i].append(temp)
                        temp1.append(temp)
            res[i].append([nums[i]])
            
        temp1 = list(set((map(tuple, temp1))))
        
        return temp1