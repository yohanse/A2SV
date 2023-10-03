class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if not stack or stack[-1][0] != i:
                stack.append([i, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        ans = ""
        for i, v in stack:
            ans += i * v
        return ans        