food = [[[0], [1], [2], [0, 1], [0, 2], [1, 2], [0, 1, 2]], 
        [[0], [1], [2], [0, 1], [1, 2], [0, 2], [0, 1, 2]],
        [[0], [1], [2], [0, 2], [0, 1], [1, 2], [0, 1, 2]],
        [[0], [1], [2], [0, 2], [1, 2], [0, 1], [0, 1, 2]],
        [[0], [1], [2], [1, 2], [0, 1], [0, 2], [0, 1, 2]],
        [[0], [1], [2], [1, 2], [0, 2], [0, 1], [0, 1, 2]]]

t = int(input())
for _ in range(t):
    ans = 0
    count1 = list(map(int, input().split()))
    answer = 0
    for k in range(6):
        ans = 0
        count = count1.copy()
        for i in food[k]:
            temp = count.copy()
            for j in i:
                count[j] -= 1
                if count[j] == -1:
                    count = temp
                    break
                
            else:
                ans += 1
        answer = max(answer, ans)

    print(answer)