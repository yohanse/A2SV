class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1, 0)])
        visite = set([(0, 1)])
        while q:
            pos, speed, count = q.popleft()

            if pos == target:
                return count

            if (pos + speed, speed * 2) not in visite:
                q.append((pos + speed, speed * 2, count + 1))
                visite.add((pos + speed, speed * 2))

            if speed > 0:
                if (pos, -1) not in visite:
                    visite.add((pos, -1))
                    q.append((pos, -1, count + 1))

            else:
                if (pos, 1) not in visite:
                    visite.add((pos, 1))
                    q.append((pos, 1, count + 1))