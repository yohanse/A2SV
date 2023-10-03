n, k = list(map(int, input().split()))

string = input()
dic = [0, 0]
l = ans = 0
for r in range(n):
    dic[ord(string[r]) - ord("a")] += 1
    while min(dic) > k:
        dic[ord(string[l]) - ord("a")] -= 1
        l += 1
    ans = max(ans, r - l + 1)
print(ans)
    