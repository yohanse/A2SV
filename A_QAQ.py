dp = {}
def dynamic(i, j, string, test):
    if j == 3:
        return 1
    
    if i == len(string):
        return 0
    
    if (i, j) in dp:
        return dp[(i, j)]
    
    dp[(i, j)] = dynamic(i + 1, j, string, test)
    if test[j] == string[i]:
        dp[(i, j)] += dynamic(i + 1, j + 1, string, test)

    return dp[(i, j)]

print(dynamic(0, 0, input(), "QAQ"))