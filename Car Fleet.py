class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N=len(position)
        for i in range(N):
            position[i]=[position[i],speed[i]]
        position.sort(reverse=True)
        stack=[]
        for p,s in position:
            t=(target-p)/s
            stack.append(t)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)