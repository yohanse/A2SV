s = input()
t = input()

l = -1

while -l <= min(len(s), len(t)) and s[l] == t[l]:
    l -= 1


print(len(s) + len(t) + 2 * (l + 1))
