test = int(input())
res = {}
for i in range(test):
    word = input()
    res[word] = res.get(word,0) + 1
print(len(res))
for i in res:
    print(res[i], end=' ')
print()