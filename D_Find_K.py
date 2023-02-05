t = int(input())
for i in range(t):
    n,k = list(map(int,input().split()))
    num = list(map(int,input().split()))
    num = num + [k]
    num.sort()
    print(num)