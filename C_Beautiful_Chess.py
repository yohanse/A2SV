t = int(input())
t = t*9
res = []
for i in range(t):
    
    n = input()
    
    if n != '':
        res.append(n)
    else:
        
        if res != []:
            
            
            for i in range(1, 7):
                for j in range(1, 7):
                    if res[i][j] == '#' and res[i + 1][j + 1] == '#' and res[i - 1][j + 1]=='#' and res[i + 1][j - 1]=='#' and res[i - 1][j - 1]=='#':
                        print(i + 1,j + 1)
                        break
            res = []
for i in range(1, 7):
    for j in range(1, 7):
        if res[i][j] == '#' and res[i + 1][j + 1] == '#' and res[i - 1][j + 1]=='#' and res[i + 1][j - 1]=='#' and res[i - 1][j - 1]=='#':
                print(i + 1,j + 1)
                break