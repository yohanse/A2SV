# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(T):
    n = int(input())
    cube = list(map(int,input().split()))
    N = len(cube)
    if N == 1:
        print("Yes")
    else:
        base = max(cube[0], cube[-1])
        left, right = 0, N-1
        while right>=left:
            if cube[left] <= base and cube[right] <= base:
                if cube[left] > cube[right]:
                    base = cube[left]
                    left += 1
                else:
                    base = cube[right]
                    right -= 1
            else:
                print("No")
                break
        else:
            print("Yes")