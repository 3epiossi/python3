class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = MountainArray.length(mountain_arr)
        l, r = 0, length-1
        L, R = l, r
        h = 0
        while l < r:
            h = (l+r)//2
            data, data1 = \
        MountainArray.get(mountain_arr,h), MountainArray.get(mountain_arr,h+1)
            if data < data1:
                l = h+1
            else:
                r = h

        
        M = (L+R)//2
        data = 0
        l, r = L, h
        while l < r:
            m = (l+r)//2
            data = MountainArray.get(mountain_arr,m)
            if data < target:
                l = m+1
            elif target < data:
                r = m
            else:
                return m
        if MountainArray.get(mountain_arr,l) == target:
            return l
        l, r = h, R
        while l < r:
            m = (l+r)//2
            data = MountainArray.get(mountain_arr,m)
            if data > target:
                l = m+1
            elif target > data:
                r = m
            else:
                return m
        if MountainArray.get(mountain_arr,l) == target:
            return l
        return -1

