class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[b].append(a)
            graph[a].append(b)
        res = []
        for z in adjacentPairs:
            for i in z:
                if len(graph[i]) == 1:
                    p, v = None, i
                    for i in range(len(adjacentPairs) + 1):
                        res.append(v)
                        for a in graph[v]:
                            if a != p:
                                p, v = v, a
                                break
                    break
            if res:
                break

        return res