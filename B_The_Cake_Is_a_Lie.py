dp = {}
def dynamic(i, j, k, n, m):
    if i == n and m == j:
        return 0 == k

    if i == n + 1 or j == m + 1:
        return False
    
    if (i, j, k) in dp:
        return dp[(i, j, k)]
    
    dp[(i, j, k)] = dynamic(i + 1, j, k - j, n, m) or dynamic(i, j + 1, k - i, n, m)
    return dp[(i, j, k)]

for _  in range(int(input())):
    n, m, k = list(map(int, input().split()))
    dp = {}
    if dynamic(1, 1, k, n, m):
        print("YES")
    else:
        print("NO")
