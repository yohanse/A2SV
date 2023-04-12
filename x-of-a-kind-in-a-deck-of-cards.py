class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        for i in count:
            prev = count[i]
            break

        for i in count:
            prev = gcd(prev, count[i])


        return False if prev == 1 else True