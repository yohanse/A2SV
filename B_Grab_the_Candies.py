t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    even = 0
    for i in num:
        if i % 2:
            even += i
    if sum(num) -  even > even:
        print("YES")
    else:
        print("NO")