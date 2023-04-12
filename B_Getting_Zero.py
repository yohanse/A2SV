def dfs(x, c, maxi):
    while 2 * x < 32768:
        

n = int(input())
nums = list(map(int, input().split()))
for i in range(n):
    x = nums[i]
    print(dfs(x, 0, 32768 - x))