# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
english = set(input().split())
f = int(input())
french = set(input().split())
ans = english - french
print(len(ans))