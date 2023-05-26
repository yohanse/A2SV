class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def union(self, a, b):
        px, py = self.find(a), self.find(b)
        if px != py:
            if px < py:
                self.parent[py] = px   
            else:
                self.parent[px] = py
            
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        disjoint = Disjoint(26)
        for i in range(len(s1)):
            disjoint.union(ord(s1[i]) - 97, ord(s2[i]) - 97)
        ans = ""
        for i in baseStr:
            ans += chr(disjoint.find(ord(i) - 97) + 97)
        return ans