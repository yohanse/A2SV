from collections import deque
n, k = list(map(int, input().split()))
temp = n
answer = []
c = 0
while temp:
    if temp & 1:
        answer.append(2 ** c)
    temp = temp >> 1
    c += 1


answer = deque(answer)
have = len(answer)
while have < k:
    if answer[-1] == 1:
        break
    last = answer.pop()
    if last == 2:
        answer.appendleft(1)
        answer.appendleft(1)
    else:
        answer.append(last // 2)
        answer.append(last // 2)
    have += 1
    
answer = list(answer)
answer.sort()
if have == k:
    print("YES")
    print(*answer)
else:
    print("NO")
