from collections import defaultdict
testCase = int(input())
for i in range(testCase):
    size = int(input())
    nums = input().split()
    string = input()
    table = defaultdict(set)
    for i in range(size):
        table[nums[i]].add(string[i])
        if len(table[nums[i]]) == 2:
            print("No")
            break
    else:
        print("Yes")