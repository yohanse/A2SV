class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        num = tickets[k]

        N = len(tickets)
        tot = tickets[k]
        for i in range(N):
            if i < k:
                tot += min(num, tickets[i])
            elif i > k:
                tot += min(num - 1, tickets[i])
        return tot