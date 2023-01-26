import sys
n, k = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()
num = [1] + num + [sys.maxsize]


if num[k + 1] - num[k] > 0:
    print(num[k])
else:
    print(-1) 