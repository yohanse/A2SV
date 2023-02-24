n = int(input())
num = list(map(int, input().split()))
num.sort()

l = 0
ans = 1
for r in range(n):
    while num[r] - num[l] > 5:
        l += 1
    ans = max(ans, r - l + 1)
print(ans)
