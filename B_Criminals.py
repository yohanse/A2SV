t = int(input())
for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    curr = 0
    for i in range(n - 1):
        if curr > 0 and num[i] == 0:
            curr += 1
        elif num[i] != 0:
            curr += num[i]
    print(curr)