n = int(input())
num = list(map(int, input().split()))
num.sort()
op = "NO"
for i in range(n - 2):
    if num[i] + num[i+1] > num[i+2] and num[i] + num[i+2] > num[i+1] and num[i + 2] + num[i+1] > num[i]:
        op = "YES"
print(op)
