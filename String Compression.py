class Solution:
    def compress(self, chars: List[str]) -> int:
        store=chars[0]
        ans=len(chars)
        count=0
        for i in range(ans):
            if chars[0]!=store:
                chars.append(store)
                if count>1:
                    count=str(count)
                    for i in range(len(count)):
                        chars.append(count[i])
                count=0
                store=chars[0]
            chars.pop(0)
            count=count+1
        chars.append(store)
        if count!=1:
            count=str(count)
            for i in range(len(count)):
                chars.append(count[i])
        return len(chars)
        