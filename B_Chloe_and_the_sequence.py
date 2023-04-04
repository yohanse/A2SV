n, k = list(map(int, input().split()))
mid = 2 ** (n - 1) 
root = n
while mid != k:
    if k > mid:
        k -= mid
        
    root -= 1
    mid //= 2
print(root)