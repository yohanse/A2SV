
import math


t = int(input())

for _ in range(t):
    n, d = list(map(int, input().split()))
    x1, x2 = math.ceil(math.sqrt(d)) - 1, int(math.sqrt(d)) - 1

    if d <= n or x1 + math.ceil(d / (x1 + 1)) <= n or x2 + math.ceil(d / (x2 + 1)) <= n:
        print("YES")
    else:
        print("NO")