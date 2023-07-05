test_cases = int(input())

def min_operations(str_num):
    lengthOfString = len(str_num)

    for i in range(lengthOfString, -1, -1):
        for j in range(i + 1, lengthOfString):
            if int(str_num[i] + str_num[j]) % 25 == 0:
                return lengthOfString - i - 2
            
    return -1  #if the answer does not exists


for _ in range(test_cases):
    str_num = input()
    print(min_operations(str_num)) 



# t = int(input())

# def check(n, test):
#     c = 0
#     ans = []
#     for i in range(len(n) - 1, -1, -1):
#         if test[c] == n[i]:
#             ans.append(i)
#             c += 1
#         if c == 2:
#             return ans
# for _ in range(t):
#     n = int(input())
#     res = 100
#     for k in ["00", "52", "57", "05"]:
#         ans = check(str(n), k)
#         if ans != None:
#             res = min(res, len(str(n)) - ans[0] + ans[0] - ans[1] - 2)
#     print(res)