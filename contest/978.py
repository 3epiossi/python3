class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxLen = 1
        l, r = 0, 1
        length = len(arr)
        while l < length and r < length:
            if arr[l] > arr[r]:
                alt = 1
            elif arr[l] < arr[r]:
                alt = -1
            else:
                l = r
                r = l+1
                continue
            while True:
                    if r+1 < length and alt == 1 and arr[r] < arr[r+1]:
                        r += 1
                        alt = -1
                    elif r+1 < length and alt == -1 and arr[r] > arr[r+1]:
                        r += 1
                        alt = 1
                    else:
                        break
            if r-l+1 > maxLen:
                maxLen = r-l+1
            l = r
            r = l+1
        return maxLen

            