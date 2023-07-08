class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        longlen = 0

        for i in range(len(s)):
            l, r = i-1, i+1
            permission1 = True
            l2, r2 = i-1, i
            permission2 = True
            while True:
                if permission1:
                    if not(l >= 0 and r < len(s) and s[l] == s[r]):
                        if r-l-1 > longlen:
                            longest = s[l+1: r]
                            longlen = r-l-1
                        permission1 = False
                if permission2:
                    if not(l2 >= 0 and r2 < len(s) and s[l2] == s[r2]):
                        if r2-l2-1 > longlen:
                            longest = s[l2+1: r2]
                            longlen = r2-l2-1
                        permission2 = False
                if not(permission1 or permission2):
                    break
                l, r = l-1, r+1
                l2, r2 = l2-1, r2+1
            
                
        return longest