class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        candidate = [0] * (5001)
        winner = [0] * len(times)
        winner[0] = persons[0]
        candidate[persons[0]] += 1
        self.n = len(times)

        for i in range(1, self.n):
            name = persons[i]
            candidate[name] += 1
            last = winner[i - 1]

            if candidate[name] >= candidate[last]:
                winner[i] = name
            else:
                winner[i] = last

            self.winner = winner
            self.times = times

    def q(self, t: int) -> int:
        left, right = 0, self.n - 1

        while left < right:
            mid = (left + right + 1) // 2
            if self.times[mid] > t:
                right = mid - 1
            else:
                left = mid

        return self.winner[left]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)