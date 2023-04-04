t = int(input())
for i in range(t):
    string = input()
    group = string[0]
    ans = 0
    for i in range(len(string)):
        if group != string[i]:
            ans += 1 - int(group)
            group = string[i]
    ans += 1 - int(group)
    print(min(2, int(ans)))