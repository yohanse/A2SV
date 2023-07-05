import sys


t = int(input())

for _ in range(t):
    input()

    n, k = list(map(int, input().split()))
    pos = list(map(int, input().split()))
    tem = list(map(int, input().split()))

    left  = [sys.maxsize for i in range(n)]
    right = [sys.maxsize for i in range(n)]

    for i in range(k):
        left[pos[i] - 1]  = tem[i]
        right[pos[i] - 1] = tem[i]

    for i in range(1, n):
        left[i] = min(left[i], left[i - 1] + 1)
    
    for i in range(n - 2, -1, -1):
        right[i] = min(right[i], right[i + 1] + 1)
    
    for i in range(n):
        left[i] = min(left[i], right[i])
    
    print(*left)