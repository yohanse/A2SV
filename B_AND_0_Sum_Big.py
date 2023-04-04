def power(n, k):
    if k == 1:
        return n
    if k % 2 == 1:
        return (n * (power(n, k // 2) ** 2)) % (10 ** 9 + 7)
    return (power(n, k // 2) ** 2) % (10 ** 9 + 7)

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    print(power(n, k))
