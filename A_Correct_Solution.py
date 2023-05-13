from collections import deque


n = list(input())
m = input()

if n == "0":
    if n == m:
        print("OK")
    else:
        print("WRONG_ANSWER")
else:
    for i in range(len(n)):
        if n[i] != "0":
            final = i
            break
    ans = n[final]
    for i in range(len(n)):
        if final != i:
            ans += n[i]
    if ans == m:
        print("OK")
    else:
        print("WRONG_ANSWER")
