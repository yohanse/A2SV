t = int(input())
for _ in range(t):
    n = int(input())
    nums = [4, 6, 3, 2, 0, 8, 9, 1, 7, 5]
    num = [1,0,2,3,5,4,6,7,9,8]
    
    for i in range(30):
        temp = bin(i)[2:]
        print(i, end = "==>")
        for j in range(5 - len(temp)):
            print(0, end = '')
        print(temp)

