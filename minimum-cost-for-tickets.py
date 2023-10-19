class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        
        @cache
        def dfs(index):
            if index == n:
                return 0

            return min(
                dfs(bisect_left(days, days[index] + 1)) + costs[0],
                dfs(bisect_left(days, days[index] + 7)) + costs[1],
                dfs(bisect_left(days, days[index] + 30)) + costs[2]
            )
        return dfs(0)