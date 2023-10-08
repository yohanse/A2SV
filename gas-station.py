class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        need = len(gas)
        gas, cost = gas + gas, cost + cost
        length = 2*need
        total, l = 0, 0
        for r in range(length):
            total += gas[r] - cost[r]
            if total < 0:
                total = 0
                l = r + 1
            if r - l + 1 == need:
                return l
        return -1