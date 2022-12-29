value ={'L':3, 'M':2, 'S':1, 'X':10}
testCase = int(input())
for i in range(testCase):
    shirt1, shirt2 = input().split()
    size = min(len(shirt1), len(shirt2))
    if value[shirt1[-1]] > value[shirt2[-1]]:
        print('>')
    elif value[shirt1[-1]] < value[shirt2[-1]]:
        print('<')
    else:
        if shirt1[-1] == 'S':
            if len(shirt1) > len(shirt2):
                print('<')
            elif len(shirt1) < len(shirt2):
                print('>')
            else:
                print('=')
        else:
            if len(shirt1) < len(shirt2):
                print('<')
            elif len(shirt1) > len(shirt2):
                print('>')
            else:
                print('=')
    
