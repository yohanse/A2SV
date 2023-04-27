class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        begin = "0000"
        deadends = set(deadends)

        q = deque([(begin, 0)])
        if begin in deadends:
            return -1

        while q:
            begin, count = q.popleft()
            if begin == target:
                return count

            for i in range(4):
                x = int(begin[i])

                num = (int(begin[i]) + 1) % 10
                temp = begin[:i] + str(num) + begin[i + 1:]
                
                if temp not in deadends:
                    deadends.add(temp)
                    q.append((temp, count + 1))

                x -= 1
                if x == -1:
                    x = 9
                temp = begin[:i] + str(x) + begin[i + 1:]
                if temp not in deadends:
                    deadends.add(temp)
                    q.append((temp, count + 1))

        return -1