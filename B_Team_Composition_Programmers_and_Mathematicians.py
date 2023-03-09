t = int(input())
for _ in range(t):
    pro, mat = list(map(int, input().split()))
    ans = 0
    number_of_group = (pro + mat)//4

    left, right = 0, number_of_group

    while left < right:
        mid = (left + right + 1)//2
        if min(pro, mat) < mid:
            right = mid - 1
        else:
            left = mid
            
    print(left)
    