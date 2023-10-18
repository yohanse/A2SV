class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
            
        is_prime = [True for i in range(n)]
        is_prime[0] = is_prime[1] = False
        count = 0
        for i in range(n):
            if is_prime[i]:
                k = i * i
                while k < n:
                    is_prime[k] = False
                    k += i
                count += 1
        return count