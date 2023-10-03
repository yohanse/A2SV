class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        cost = 0
        costs.sort(key = lambda x: x[0] - x[1])
        for i in range(2):
            for j in range(i * n, (i + 1) * n):
                cost += costs[j][i]
        
        return cost