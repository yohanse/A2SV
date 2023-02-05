t = int(input())
for i in range(t):
    n = input()
    N = len(n)
    i = 0
    op = [0] * 26
    l = 0
    while i < N:
        while i < N and n[i] == n[l]:
            i += 1
        if (i-l)%2 == 1:
            op[ord(n[l]) - ord('a')] = 1
        l = i
    
    pri = ''
    for i in range(26):
        if op[i] != 0:
            pri += chr(i + ord('a'))
    print(pri)