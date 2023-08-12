t = int(input())

for _ in range(t):
    a, b = input().split()
    
    letter = [0 for i in range(26)]
    for i in b:
        letter[ord(i) - ord('a')] += 1
    ans = 0
    for i in a:
        if letter[ord(i) - ord('a')] != 0:
            letter[ord(i) - ord('a')] -= 1
            ans += 1
        else:
            break
    print(ans)