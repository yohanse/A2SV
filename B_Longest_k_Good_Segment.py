n, k = list(map(int, input().split()))
num = list(map(int, input().split()))
dic = {}
have = 0
l = 0
ans = [0, 0]
for i, number in enumerate(num):
    dic[number] = dic.get(number, 0) + 1
    if dic[number] == 1:
        have += 1

    while have > k:
        number = num[l]
        dic[number] -= 1
        if dic[number] == 0:
            have -= 1
        l += 1
    if ans[1] - ans[0] < i - l:
        ans = [l, i]

print(ans[0] + 1, ans[1] + 1)
    