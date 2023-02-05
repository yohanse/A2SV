s = input()

stack = []
remove = False
valid = []
l, r = 0, len(s) - 1
count = 0

while l < r:
    if s[l] != "(":
        l += 1
    if s[r] != ")":
        r -= 1
    if l < r and s[l] == "(" and s[r] == ")":
        valid.append(str(l + 1))
        valid.append(str(r + 1))
        l += 1
        r -= 1
if len(valid) != 0:
    print(1)
    print(len(valid))
    valid = list(map(int, valid))
    valid.sort()
    valid = list(map(str, valid))
    print(" ".join(valid))
else:
    print(0)
    

