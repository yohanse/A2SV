class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        need, have, letter = 0, 0, [0]*26
        count = Counter(s)
        res = []

        h = 0
        for i, l in enumerate(s):

            count[l] -= 1
            letter[ord(l) - ord("a")] += 1

            if count[l] == 0:
                have += 1

            if letter[ord(l) - ord("a")] == 1:
                need += 1

            if need == have:
                res.append(i - h + 1)
                h = i + 1

        return res