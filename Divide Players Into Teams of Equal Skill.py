class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)
        skill.sort()
        team = skill[0] + skill[-1]
        left, right =  1, N - 2
        res = skill[0]*skill[-1]
        while left < right:
            if skill[left] + skill[right] != team:
                return -1
            res += skill[left]*skill[right]
            left += 1
            right -= 1
        return res