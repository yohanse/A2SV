value ={'L':3, 'M':2, 'S':1, 'X':10}
testCase = int(input())
for i in range(testCase):
    shirt1, shirt2 = input().split()
    size = min(len(shirt1), len(shirt2))
    for j in range(size):
        if shirt1[j]=='X' or shirt2[j]=='X':
            p1 = p2 = j
            while shirt1[p1] == 'X':
                p1 += 1
            while shirt2[p2] == 'X':
                p2 += 1
            if value[shirt1[j]] > value[shirt2[j]]:
                print('>')
            elif value[shirt1[j]] < value[shirt2[j]]:
                print('<')
            elif 
            
        elif value[shirt1[j]] > value[shirt2[j]]:
            print('>')
        elif value[shirt1[j]] < value[shirt2[j]]:
            print('<')
