def solve():
    mod = 10**9 + 7
    t = int(input())
    for _ in range(t):
        n, k = map(int,input().split())
        ans = pow(2*k-1,n,mod)
        print(ans)

solve()