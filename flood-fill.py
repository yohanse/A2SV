class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack,dcolor,row,col=[(sr,sc)],image[sr][sc],len(image),len(image[0])
        image[sr][sc]=color
        while stack:
            r,c=stack.pop()
            for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
                nr,nc=r+i,c+j
                if -1<nr<row and -1<nc<col and image[nr][nc] != color and image[nr][nc] == dcolor :
                    stack.append((nr,nc))
                    image[nr][nc]=color
        return image