import sys
n, k = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()
num = [0] + num + [sys.maxsize]


if num[k + 1] - num[k] > 1 and num[k] != 10**9:
    print(num[k] + 1)
else:
    print(-1) 