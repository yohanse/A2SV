class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(numbers)):
            if target - numbers[i] in data:
                return [data[target - numbers[i]] + 1, i + 1]
            data[numbers[i]] = i
        