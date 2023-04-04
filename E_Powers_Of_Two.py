n, k = list(map(int, input().split()))
temp = n
answer = []
c = 0
while temp:
    if temp & 1:
        answer.append(2 ** c)
    temp = temp >> 1
    c += 1
 
def expand(nums):
    real = [0] * k
    need = k - len(nums)
    
            
 
if len(answer) > k or  k > n:
    print("NO")
else:
    