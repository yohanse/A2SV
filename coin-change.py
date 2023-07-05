class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [sys.maxsize] * (amount + 1)
        arr[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if i - j > -1:
                    arr[i] = min(1 + arr[i - j], arr[i])
        return arr[-1] if arr[-1] != sys.maxsize else -1