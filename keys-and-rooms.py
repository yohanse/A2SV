class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visite = set([0])

        res = 0
        while q:
            vertex = q.popleft()
            for adjvertex in rooms[vertex]:
                if adjvertex not in visite:
                    q.append(adjvertex)
                    visite.add(adjvertex)
            res += 1
        
        return res == len(rooms)