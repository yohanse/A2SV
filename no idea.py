n, m = map(int,input().split())
happy = input().split()
A = set(input().split())
B = set(input().split())
happiness = 0
for i in happy:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
print(happiness)