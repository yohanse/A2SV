class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        def function(img1, img2):
            n = len(img1)
            dic = {0:0}
            for x in range(n):
                for y in range(n):
                    for r in range(n):
                        for c in range(n):
                            if img1[x][y] == img2[r][c] == 1:
                                dic[(x - r, y - c)] = dic.get((x - r, y - c), 0) + 1
            return max(dic.values())
        return max(function(img1, img2), function(img2, img1))