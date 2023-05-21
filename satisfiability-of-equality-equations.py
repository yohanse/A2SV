class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        Group=[i for i in "abcdefghijklmnopqrstuvwxyz"]

        def find(var):
            if Group[ord(var)-97]==var:return var
            return find(Group[ord(var)-97])

        def union(var1,var2):
            p1,p2=find(var1),find(var2)
            Group[ord(p1)-97]=p2
                
        for var1,sign,normal,var2 in equations:
            if sign=="=":
                union(var1,var2)
        
        for var1,sign,normal,var2 in equations:
            if sign=="!" and find(var1)==find(var2):
                return False

        return True