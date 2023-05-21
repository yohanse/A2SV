class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        Graph=defaultdict(list)
        for x,y in stones:
            Graph[x].append([x,y])
            Graph[~y].append([x,y])
        groups=0
        visite=set()
        for i,j in stones:
            if  not (i,j) in visite:
                visite.add((i,j))
                groups+=1
                stack=[[i,j]]
                while stack:
                    i,j=stack.pop()
                    for x,y in Graph[i]:
                        if not (x,y) in visite:
                            stack.append([x,y])
                            visite.add((x,y))
                    for x,y in Graph[~j]:
                        if not (x,y) in visite:
                            stack.append([x,y])
                            visite.add((x,y))
        return len(stones)-groups