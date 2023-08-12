s = set([0])
for i in [10, 20, 50, 100]:
    temp = s.copy()

    for j in temp:
        for k in range(1, 5):
            s.add(j + k * i)
print(len(s))