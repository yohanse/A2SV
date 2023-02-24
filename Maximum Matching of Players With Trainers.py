class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p, t, N, n = 0, 0, len(players), len(trainers)
        while p < N and t < n:
            if players[p] <= trainers[t]:
                p += 1
            t += 1
        return p