n = int(input())
nums = list(map(int, input().split()))
ans = max(nums) - min(nums)
ans = [0 for i in range(n)]
pre = [0 for i in range(n)]
res = [0 for i in range(n)]


for i in range(1, n):
    ans[i - 1] = max(nums[i] - nums[i - 1], 0)
    pre[i] = max(nums[i] - nums[i - 1], 0)


for i in range(1, n):
    pre[i] += pre[i - 1]

for i in range(n - 2, -1, -1):
    ans[i] += ans[i + 1]

for i in range(n):
    res[i] = pre[i] + ans[i] + nums[i]



maxi = 0
answer = 0
for i in range(1, n):
    answer = max(answer, res[maxi] - nums[i] + ans[i] - ans[maxi])
    if res[i] > maxi:
        maxi = i
for i in range(n):
    answer = max(answer, ans[i] + 2 * pre[i])
print(answer)
    