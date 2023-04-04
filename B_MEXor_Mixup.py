def computeXOR(n) :
    if n % 4 == 0 :
        return n
    if n % 4 == 1 :
        return 1
    if n % 4 == 2 :
        return n + 1
    return 0

t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    xor = computeXOR(a - 1)
    
    res = 0
    if xor != b:
        plan = xor ^ b
        if plan == a:
            res += 1
        res += 1
    print(a + res)