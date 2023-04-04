t = int(input())
for _ in range(t):
    string = input()
    answer = "NO"
    for i in range(1, 7):
        count = 0

        for j in string:
            index = ord("C") - ord(j)
            if (1 << index) & i:
                count += 1
            else:
                count -= 1

            if count < 0:
                break
        else:
            if count == 0:
                answer = "YES"
    print(answer)
    