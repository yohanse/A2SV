a, b = list(map(int, input().split()))
def dfs(a, b, ans = []):
    if a == b:
        ans.append(a)
        return ans
    
    if a > b:
        return False
    
    ans.append(a)
    l = dfs(a * 2, b, ans)
    if l:
        return l
    
    r = dfs(a * 10 + 1, b, ans)
    if r:
        return r
    ans.pop()
    return False

ans = dfs(a, b)
if ans == False:
    print("NO")
else:
    print("YES")
    print(len(ans))
    print(*ans)