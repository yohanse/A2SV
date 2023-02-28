class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def rec(n, list1):
            if n == 0:
                return list1

            a = self.invert(list1.copy())
            a = a[::-1]
            list1 = list1 + ['1'] + a
        
            return rec(n - 1, list1)
        
        return rec(n, ['0'])[k - 1] 


    def invert(self, list1):
        for i in range(len(list1)):
            if list1[i] == '1':
                list1[i] = '0'
            else:
                list1[i] = '1'
        return list1
