n, d = list(map(int, input().split()))
num = list(map(int, input().split()))

num.sort(reverse = True)

answer = 0
team_tot = 0
for i in range(n):
    team_tot += d // num[i] + 1
    
    if team_tot > n:
        break

    answer += 1
print(answer)