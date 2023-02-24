class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] *(len(s) + 1)
        for start, end, direction in shifts:
            if not direction:
                direction = -1
            prefix_sum[start] += direction
            prefix_sum[end + 1] -= direction
            
        for i in range(1,len(s)):
            prefix_sum[i] += prefix_sum[i - 1]

        answer = ""
        for index, letter in enumerate(s):
            shift = (ord(letter) - ord("a") + prefix_sum[index]) % 26
            answer += chr(shift + ord("a"))

        return answer