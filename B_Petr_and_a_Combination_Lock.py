n = int(input())
num = [0] * n
for i in range(n):
    num[i] = int(input())

def recur(index, ans, n):
    if index == n:
        return ans % 360 == 0

    return recur(index + 1, ans + num[index], n) or recur(index + 1, ans - num[index], n)
operation = "NO"
if recur(0, 0, n):
    operation = "YES"
print(operation)