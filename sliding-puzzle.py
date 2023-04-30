class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        string = ""
        for i in range(2):
            for j in range(3):
                string += str(board[i][j])
                if board[i][j] == 0:
                    start = i * 3 + j

        visite = set([string])
        q = deque([(string, 0, start)])
        while q:
            string, count, start = q.popleft()
            if string == "123450":
                return count

            for x in [-3, 3, -1, 1]:
                new_start = start + x
                if (x == 1 and start == 2) or (x == -1 and start == 3):
                    continue
                if -1 < new_start < 6:

                    if new_start > start:
                        new_string = string[:start] + string[new_start] + string[start + 1:new_start] + "0" + string[new_start + 1:]
                    else:
                        new_string = string[:new_start] + "0" + string[new_start + 1:start] + string[new_start] + string[start + 1:]
                    
                    if new_string not in visite:
                        q.append((new_string, count + 1, new_start))
                        visite.add(new_string)
        return -1