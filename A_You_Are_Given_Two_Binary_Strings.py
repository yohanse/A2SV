t = int(input())
for _ in range(t):
    x = input()
    y = input()
    x = x[::-1]
    y = y[::-1]
    for i in range(len(y)):
        if y[i] == "1":
            best = i
            break
    for i in range(best, len(x)):
        if x[i] == "1":
            print(i - best)
            break