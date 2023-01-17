n = int(input())
num = list(map(int,input().split()))
n1, n2, n3 = [], [], []
for i in range(n):
    if num[i] < 0:
        n1.append(str(num[i]))
    elif num[i] > 0:
        n2.append(str(num[i]))
    else:
        n3.append(str(num[i]))

if len(n2) == 0:
    n2.append(n1.pop()) 
    n2.append(n1.pop())  
if len(n1) % 2 == 0:
    n3.append(n1.pop())

n1 = [str(len(n1))] + n1
n2 = [str(len(n2))] + n2
n3 = [str(len(n3))] + n3
print(' '.join(n1))
print(' '.join(n2))
print(' '.join(n3))

