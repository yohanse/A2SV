n, k = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()

left, right = 0, 2**n - 1

while left < right:
    a = max(max())