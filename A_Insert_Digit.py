t = int(input())
for _ in range(t):
    n, d = list(map(int, input().split()))
    num = input()
    
    ans = 0
    for i in range(n):
        if d > int(num[i]):
            print(num[:i] + str(d) + num[i:])
            break
    else:
        print(num + str(d))