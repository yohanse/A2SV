class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd, even = {-1: 0}, {-1: 0}
        n = len(nums)
        
        def pickTwoMax(dictionary):
            ans = [[-1, -1], [-1, -1]]

            for i in dictionary:
                if ans[0][1] < dictionary[i]:
                    ans[1] = ans[0].copy()
                    ans[0] = [i, dictionary[i]]
                elif ans[1][1] < dictionary[i]:
                    ans[1] = [i, dictionary[i]]
            
            return ans

        for i in range(len(nums)):
            if i % 2:
                odd[nums[i]] = odd.get(nums[i], 0) + 1
            else:
                even[nums[i]] = even.get(nums[i], 0) + 1
        
        even = pickTwoMax(even)
        odd = pickTwoMax(odd)

        ans = n
        for x, y in even:
            for i, j in odd:
                if i != x:
                    ans = min((n // 2 + n % 2 - y) + (n // 2 - j), ans)
        return ans