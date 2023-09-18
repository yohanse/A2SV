class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        l, r = 1, 10 ** 8
        n, m = len(dungeon), len(dungeon[0])

        def check(k, dungeon):
            dungeon1 = copy.deepcopy(dungeon)
            if -dungeon[0][0] >= k:
                return False
            
            state = [[False for i in range(m)] for j in range(n)]
            state[0][0] = True

            dungeon1[0][0] += k

            for i in range(n):
                for j in range(m):
                    if i == j == 0:
                        continue
                    elif i == 0:
                        if state[i][j - 1] and dungeon1[i][j - 1] + dungeon1[i][j] > 0:
                            state[i][j] = True
                            dungeon1[i][j] += dungeon1[i][j - 1]
                    elif j == 0:
                        if state[i - 1][j] and dungeon1[i - 1][j] + dungeon1[i][j] > 0:
                            state[i][j] = True
                            dungeon1[i][j] += dungeon1[i - 1][j]
                        
                    else:
                        count = dungeon[i][j]
                        if state[i - 1][j] and dungeon1[i - 1][j] + dungeon1[i][j] > 0:
                            state[i][j] = True
                            dungeon1[i][j] += dungeon1[i - 1][j]

                        if state[i][j - 1] and dungeon1[i][j - 1] + dungeon1[i][j] > 0:
                            state[i][j] = True
                            dungeon1[i][j] = max(dungeon1[i][j - 1] + count, dungeon1[i][j])
            return state[-1][-1]
        while r > l:
            mid = (r + l) // 2
            

            if check(mid, dungeon):
                r = mid
            else:
                l = mid + 1
        return r
        