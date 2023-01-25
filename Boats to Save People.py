class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:
            if limit >= people[l] + people[r]:
                l += 1
            r -= 1
        return len(people) - r - 1
                    