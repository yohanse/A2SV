class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        @cache
        def dfs(i, isChanged):
            if i == n:
                return 0

            if isChanged:
                if nums1[i] <= nums2[i - 1] or nums2[i] <= nums1[i - 1]:
                    return dfs(i + 1, True) + 1

                if nums1[i] <= nums1[i - 1] or nums2[i] <= nums2[i - 1]:
                    return dfs(i + 1, False)
                    
                return min(dfs(i + 1, True) + 1, dfs(i + 1, False))

            I_can_swap = inf
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                I_can_swap = dfs(i + 1, True) + 1

            I_can_move = inf
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                I_can_move = dfs(i + 1, False)

            return min(I_can_swap, I_can_move)
        return min(dfs(1, True) + 1, dfs(1, False))