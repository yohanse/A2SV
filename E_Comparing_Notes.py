a = input()
b = input()

check = True
for i in range(min(len(a), len(b))):
    if a[i] == "-" or b[i] == "-":
        check = True
        break
    elif a[i] != b[i]:
        check = False
        break
else:
    if len(a) != len(b):
        check = False
    else:
        check = True

if not check:
    print("NO")
else:
    a = a[::-1]
    b = b[::-1]
    for i in range(min(len(a), len(b))):
        if a[i] == "-" or b[i] == "-":
            check = True
            break
        elif a[i] != b[i]:
            check = False
            break
    else:
        if len(a) != len(b):
            check = False
        else:
            check = True
    if check:
        print("YES")
    else:
        print("NO")