class Solution:
    def printVertically(self, s: str) -> List[str]:
        res=s.split()
        string_length = 0
        result = []
        for i in range(len(res)):
            string_length = max(len(res[i]),string_length)
        for col in range(string_length):
            temp = []
            for row in range(len(res)):
                if len(res[row])>col:
                    temp.append(res[row][col])
                else:
                    temp.append(' ')
            for i in range(len(res)-1,-1,-1):
                if temp[i] == ' ':
                    temp.pop()
                else:
                    break
            temp = ''.join(temp)
            result.append(temp)
        return result