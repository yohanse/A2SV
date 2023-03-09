n = int(input())
name = input().split()
k = int(input())
for i in range(k):
    target = input()
    left, right = 0, n
    while left < right:
        mid = (left + right)//2

        if name[mid] < target:
            left = mid + 1
        else:
            right = mid
    print(left)