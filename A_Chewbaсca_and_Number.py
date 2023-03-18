x = input()
res = ''
for i in range(1, len(x)):
    if int(x[i]) > 4:
        res += str(int(9 - int(x[i])))
    else:
        res += x[i]

if int(x[0]) > 4:
    if x[0] == '9':
        res = '9' + res
    else:
        res = str(int(9 - int(x[0]))) + res
else:
    res = x[0] + res

print(res)