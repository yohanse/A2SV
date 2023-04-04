n = input()
N = len(n) 
index = 0
for i in range(N):
    if n[i] == "7":
        index += 2 ** (N - i - 1)
print(2 ** N - 2 + index + 1)
