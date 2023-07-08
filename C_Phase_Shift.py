from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    dp = {}
    connection = [i for i in range(26)]
    def find(a):
        while a != connection[a]:
            a = connection[a]
        return a
    
    used = set()
    ans = ""
    for i in s:
        if i in dp:
            ans += dp[i]
        else:
            for j in range(26):
                if j not in used:
                    if find(j) != find(ord(i) - ord('a')):
                        ans += chr(j + ord('a'))
                        dp[i] = chr(j + ord('a'))
                        used.add(j)
                        connection[find(ord(i) - ord('a'))] = connection[find(j)]
                        break
                    if len(dp) == 25:
                        ans += chr(j + ord('a'))
                        dp[i] = chr(j + ord('a'))
                        break
                
    print(ans)