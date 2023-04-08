a, b, c = list(map(int, input().split()))

# a = x + y
# b - x = c - y

# b - c = x - y
# a = x + y
# a + b - c = 2 * x

# x = (a + b - c) / 2


if (a + b - c) % 2 == 0:
    x = (a + b - c) // 2
    y = a - x
    bond1, bond2, bond3 = x, b - x, y
    if bond1 > -1 and bond2 > -1 and bond3 > -1:
        count  = 0
        if bond1 == 0:
            count += 1
        
        if bond2 == 0:
            count += 1
        
        if bond3 == 0:
            count += 1

        if count < 2:
            print(bond1, bond2, bond3)
        else:
            print("Impossible")
    else:
        print("Impossible")
else:
    print("Impossible")