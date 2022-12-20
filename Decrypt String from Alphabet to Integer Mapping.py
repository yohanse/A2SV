class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i] != "#":
                stack.append(chr(int(s[i])+96))
            else:
                stack.pop()
                stack.pop()
                stack.append(chr(int(s[i-2:i])+96))
        return ''.join(stack)