import sys


t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2:
        if n == 3:
            mini = 7
        else:
            one = "1" * ((n - 3) // 2)
            mini = int("7" + one)
    else:
        one = "1" * (n // 2)
        mini = int(one)
    

    
   
    
    dp = [str(sys.maxsize) for i in range(n + 1)]
    dp[0] = ""

    segment = [6, 2, 5, 5, 4, 4, 6, 3, 7, 6]

    for i in range(1, n + 1):
        for j in range(10):
            if i - segment[j] > -1:
                if i:
                    dp[i] = str(min(int(dp[i]), int(dp[i - segment[j]] + str(j)),  int(str(j) + dp[i - segment[j]])))
                else:
                    dp[i] = str(min(int(dp[i]), int(dp[i - segment[j]] + str(j))))
    print(dp[-1], mini)