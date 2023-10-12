# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def peakElement():
            l, r = 1, mountain_arr.length() - 2

            while l < r:
                mid = (l + r) // 2
                one, two, three = mountain_arr.get(mid - 1), mountain_arr.get(mid), mountain_arr.get(mid + 1)
                if one < two > three:
                    return mid
                elif one < two:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
            

        peakIndex = peakElement()
        l, r = 0, peakIndex
        while l < r:
            mid = (l + r + 1) // 2
            one = mountain_arr.get(mid)

            if one > target:
                r = mid - 1
            else:
                l = mid

        if mountain_arr.get(l) == target:
            return l

        l, r = peakIndex, mountain_arr.length() - 1
        while l < r:
            mid = (l + r) // 2
            one = mountain_arr.get(mid)

            if one > target:
                l = mid + 1
            else:
                r = mid
        
        if mountain_arr.get(l) == target:
            return l

        return -1