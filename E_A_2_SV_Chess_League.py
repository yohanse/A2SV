n, k = list(map(int, input().split()))
score = list(map(int, input().split()))
list = [[i] for i in range(2 ** n)]
res = []

for count in range(n):
    power = n - count - 1
    size = 2**(power + 1)
    temp = [[] for i in range(2**power)]
    for i in range(0, size, 2):
       
        copy = []
        

        num = 1000000
        for j in list[i + 1]:
            num = min(num, score[j])

        for j in list[i]:
            if score[j] + k >= num:
                copy.append(j)

        num = 1000000
        for j in list[i]:
            num = min(num, score[j])

        for j in list[i + 1]:
            if score[j] + k >= num:
                copy.append(j)
        temp[i//2] = copy.copy()

    list = temp.copy()

for i in list[0]:
    print(i + 1, end = " ")


        

             
