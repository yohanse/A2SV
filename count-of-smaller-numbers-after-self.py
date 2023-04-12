class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        nums = [[nums[i], i] for i in range(len(nums))]
        def merge(nums):
            if len(nums)==1:
                return nums
            mid = len(nums) // 2
            left = merge(nums[:mid])
            right = merge(nums[mid:])
            right.append([sys.maxsize, -1])
            n, m = len(right), len(left)
            l, r = 0, 0
            while r < n and l < m:
                if right[r][0] >= left[l][0]:
                    ans[left[l][1]] += r
                    l += 1
                else:
                    r += 1
            right.pop()

            return combo(left, right)

        def combo(left,right):
            l, r, ans = 0, 0, []
            left.append([sys.maxsize, -1])
            right.append([sys.maxsize, -1])
            while l<len(left) and r<len(right):
                if left[l][0]<right[r][0]:
                    ans.append([left[l][0], left[l][1]])
                    l += 1
                else:
                    ans.append([right[r][0], right[r][1]])
                    r += 1
            ans.pop()
            return ans
        
        merge(nums)
        return ans