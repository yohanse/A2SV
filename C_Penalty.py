def fast(nums):
    p1, p2 = 0, 0
    for i in range(10):
        if i % 2 == 1:
            p1 += int(nums[i])
        else:
            p2 += int(nums[i])
        if i % 2 == 1:
            if max(p1, p2) > min(p1, p2) + 5 - (i + 1) // 2:
                return i + 1
        else:
            if p2 > p1 + 5 - i // 2:
                return i + 1
            if p1 > p2 + 4 - i // 2:
                return i + 1

    return 10




t = int(input())
for _ in range(t):
    kicks = list(input())

    #player1 lose and player2 win

    player2_win = kicks.copy()

    for i in range(10):
        if player2_win[i] == "?":
            if i % 2 == 0:
                player2_win[i] = "0"
            else:
                player2_win[i] = "1"

    player1_win = kicks.copy()
    for i in range(10):
        if player1_win[i] == "?":
            if i % 2 == 1:
                player1_win[i] = "0"
            else:
                player1_win[i] = "1"

    print(min(fast(player1_win), fast(player2_win)))
