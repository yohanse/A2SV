class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        @cache
        def rec(t1, t2):
            if t1 == n1 or t2 == n2:
                return 0
            
            if nums1[t1] == nums2[t2]:
                return rec(t1 + 1, t2 + 1) + 1
            return max(rec(t1 + 1, t2), rec(t1, t2 + 1))
        return rec(0, 0)