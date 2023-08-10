class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        length = len(nums)
        if p == 0 or length < 2:
            return 0
        nums.sort()
        diff = []
        for i in range(length-1):
            diff.append(abs(nums[i+1]-nums[i]))
        
        mx = 10**9
        mn = 0
        length = len(diff)
        while mn < mx:
            ix = 0
            guess = (mx+mn)//2
            count = 0
            while ix < length:
                if diff[ix] <= guess:
                    count += 1
                    ix += 2
                else:
                    ix += 1
            if count >= p:
                mx = guess
            else:
                mn = guess+1
        return mx