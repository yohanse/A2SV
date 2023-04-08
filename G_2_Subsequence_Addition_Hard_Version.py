t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[0] == 1:
        curr = 1
        for i in range(1, n):
            if nums[i] > curr:
                print("NO")
                break
            curr += nums[i]
        else:
            print("YES")
    else:
        print("NO")