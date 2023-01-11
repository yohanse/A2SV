class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strings_number, strings_length, column_delete = len(strs), len(strs[0]), 0
        for col in range(strings_length):
            for row in range(1,strings_number):
                if ord(strs[row-1][col]) > ord(strs[row][col]):
                    column_delete += 1
                    break
        return column_delete