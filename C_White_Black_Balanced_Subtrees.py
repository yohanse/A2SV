import sys, threading

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        color = input()
        Tree = [[] for i in range(n)]

        for i in range(n - 1):
            Tree[nums[i] - 1].append(i + 1)
        change = {"B":1, "W":-1}
        def postorder(vertex):
            col, cou = change[color[vertex]], 0
            for adjvertex in Tree[vertex]:
                t1, t2 = postorder(adjvertex)
                col, cou = col + t1, cou + t2
            if col == 0:
                cou += 1
            return col, cou
        print(postorder(0)[1])
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()