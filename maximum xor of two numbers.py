class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        
        for num in nums:
            binary = bin(num)[2:]
            binary = "0" * (32 - len(binary)) + binary
            curr = trie
            for bit in binary:
                if bit not in curr:
                    curr[bit] = {}
                curr = curr[bit]

        ans_max = 0
        for num in nums:
            power = 2 ** 31
            binary = bin(num)[2:]
            binary = "0" * (32 - len(binary)) + binary
            ans = 0
            curr = trie
            for bit in binary:
                if str(1 - int(bit)) in curr:
                    ans += power
                    curr = curr[str(1 - int(bit))]
                elif bit in curr:
                    curr = curr[bit]
                else:
                    break
                power //= 2
            ans_max = max(ans_max, ans)

        return ans_max

