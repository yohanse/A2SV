n, k = list(map(int, input().split()))
score = list(map(int, input().split()))
check = [i for i in range(2 ** n)]

def merge(nums):
    if len(nums) == 1:
        return nums
    
    mid = len(nums) // 2
    left = merge(nums[:mid])
    right = merge(nums[mid:])
    return combine(left, right)

def combine(list, list1):
    copy = []
        
    num = 1000000
    for j in list1:
        num = min(num, score[j])

    for j in list:
        if score[j] + k >= num:
            copy.append(j)

    num = 1000000
    for j in list:
        num = min(num, score[j])

    for j in list1:
        if score[j] + k >= num:
            copy.append(j)

    return copy

ans = merge(check)
for i in ans:
    print(i + 1, end = " ")

        

             
