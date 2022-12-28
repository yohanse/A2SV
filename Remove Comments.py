class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        code = '\''.join(source)
        code += '\''
        i, temp = 0, ''
        res = []
        while i < len(code):
            if code[i:i+2] == '//' or code[i:i+2] == '/*':
                if code[i+1] == '*':
                    i += 2
                    while code[i:i+2] != '*/':
                        i += 1
                    i += 2
                else:
                    while code[i] != '\'':
                        i += 1
                    i += 1
                    if temp!='':
                        res.append(temp)
                    temp = ''
            elif code[i]=='\'':
                if temp:
                    res.append(temp)
                temp=''
                i += 1
            else:
                temp += code[i]
                i += 1
        return res