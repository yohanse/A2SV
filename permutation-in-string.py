class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


        baseHash = 1
        for i in s1:
            baseHash *= primes[ord(i) - ord("a")]
        
        currHash = 1
        for i, char in enumerate(s2):
            currHash *= primes[ord(char) - ord("a")]
            if i >= len(s1) - 1:
                if currHash == baseHash:
                    return True
                currHash //= primes[ord(s2[i - len(s1) + 1]) - ord("a")]
        return False