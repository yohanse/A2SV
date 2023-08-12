t = int(input())
for _ in range(t):
    string = input()
    string += "0"
    ans = set()

    l = 0
    for r in range(len(string)):
        if string[l] != string[r]:
            if (r - l) % 2:
                ans.add(string[l])
            l = r
    ans = list(ans)
    ans.sort()
    print("".join(ans))