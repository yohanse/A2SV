class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = [0]
        def merge(nums):
            if len(nums)==1:
                return nums
            mid = len(nums) // 2
            left = merge(nums[:mid])
            right = merge(nums[mid:])
            n, m = len(right), len(left)
            l, r = 0, 0
            while r < n and l < m:
                if right[r] * 2 < left[l]:
                    ans[0] += m -  l
                    r += 1
                else:
                    l += 1

            return combo(left, right)

        def combo(left,right):
            l, r, ans = 0, 0, []
            left.append(sys.maxsize)
            right.append(sys.maxsize)
            while l<len(left) and r<len(right):
                if left[l]<right[r]:
                    ans.append(left[l])
                    l+=1
                else:
                    ans.append(right[r])
                    r+=1
            ans.pop()
            return ans
        
        merge(nums)
        return ans[0]