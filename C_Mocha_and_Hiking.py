t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n + 1):
        print(i + 1, end = " ")
    print()