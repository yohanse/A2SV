# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))

num = int(input())
res = []

for i in range(num):
    B=set(map(int,input().split()))
    res.append(B)


check=True
  
for i in res:
    for j in i:
        if j not in A:
            check=False
    if not check:break
    
print(check)