class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        N, M, pointer = len(s), len(spaces), 0
        res = []
        for i in range(N):
            if pointer < M and i == spaces[pointer]:
                res.append(' ')
                pointer += 1
            res.append(s[i])
        return ''.join(res)
