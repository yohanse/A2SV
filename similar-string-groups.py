class Disjoint:
    def __init__(self, n):
        self.rank = [1 for i in range(n)]
        self.pare = [i for i in range(n)]
        self.group = n
    

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa != pb:
            self.group -= 1
            if self.rank[pa] == self.rank[pb]:
                self.rank[pa] += 1
            
            if self.rank[pa] > self.rank[pb]:
                self.pare[pb] = pa
            else:
                self.pare[pa] = pb
    
    def find(self, a):
        b = a
        while a != self.pare[a]:
            a = self.pare[a]
        
        while b != self.pare[b]:
            temp = self.pare[b]
            self.pare[b] = a
            b = temp
            
        return a


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)

        def isTheSame(string1, string2):
            if len(string1) != len(string2):
                return False

            if string1 == string2:
                return True
            
            index = []
            for i in range(len(string1)):
                if string1[i] != string2[i]:
                    index.append(i)
            
            if len(index) != 2 or (string1[index[-1]] != string2[index[0]]):
                return False

            return True

        disjoint = Disjoint(n)

        for i in range(n):
            for j in range(n):
                if isTheSame(strs[i], strs[j]):
                    disjoint.union(i, j)

        return disjoint.group