class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)
        def backtrack(index, condition):
            i = len(condition) - 1

            if index == N:
                if i > 1:
                    for j in range(2, i + 1):
                        if condition[j] != condition[j - 1] + condition[j - 2]:
                          
                            return False
                    return True 
                return False
           
            if i > 2 and condition[i - 1] != condition[i - 2] + condition[i - 3]:
                return False 

            if condition[-1] == 0:
                condition.append(int(num[index]))
                return backtrack(index + 1, condition)

            temp = condition.copy()
            condition[-1] = condition[-1] * 10 + int(num[index])
            temp.append(int(num[index]))
            return backtrack(index + 1, temp) or backtrack(index + 1, condition)

        return backtrack(1, [int(num[0])])