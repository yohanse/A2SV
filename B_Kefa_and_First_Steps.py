n = int(input())
num = list(map(int, input().split()))
l = 0
ans = 1
for i in range(1,n):
    if num[i - 1] > num[i]:
        l = i
    ans = max(ans, i - l + 1)
print(ans)