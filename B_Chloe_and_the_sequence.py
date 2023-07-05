n, k = list(map(int, input().split()))
mid = 2 ** (n - 1)  # we only now the middle element

while mid != k:  # the middle equals to K
    #If we find the number after the middle, we need to remove all elements before the middle.
    # This can be achieved by subtracting k by the middle index.
    if k > mid: 
        k -= mid
    n -= 1
    mid //= 2

print(n)