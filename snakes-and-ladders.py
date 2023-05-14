class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)

        def coordinate(curr):
            r =  n - 1 - (curr - 1) // n
            if ((curr - 1) // n) % 2 == 0:
                return r, ((curr - 1) % n)
            else:
                return r, n - ((curr - 1) % n) - 1
        
        q = deque([(1, 0)])
        visite = set([1])
        while q:
            vertex, count = q.popleft()
            r, c = coordinate(vertex)

            if vertex == n ** 2:
                return count
            
            for i in range(vertex + 1, min(vertex + 6, n ** 2) + 1):
                if i not in visite:
                    r, c = coordinate(i)
                    if board[r][c] == -1:
                        q.append((i, count + 1))
                    else:
                        
                        q.append((board[r][c], count + 1))
                    visite.add(i)
           
        return -1