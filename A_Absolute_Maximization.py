t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    one = [False for i in range(9)]
    zero = [True for i in range(9)]

    maxi, mini = 0, ~0
    for num in nums:
        maxi = num | maxi
        mini = num & mini

    print(maxi - mini)