t = int(input())
for i in range(t):
    d1, d2 = list(map(int,input().split()))
    d3, d4 = list(map(int,input().split()))
    if d1 + d3 == d4 == d2 or d2 + d4 == d1 == d3 or d1 + d4 == d2 == d3 or d2 + d3 == d1 == d4:
        print("Yes")
    else:
        print("No")

