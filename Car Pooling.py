class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        distance = [0] * 1001

        for n, f, t in trips:
            distance[f] += n
            distance[t] -= n
        
        for i in range(1, 1001):
            distance[i] += distance[i - 1]

        return max(distance) <= capacity