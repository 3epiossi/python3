class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(sub):
            length = len(sub)
            half = length//2
            if length == 1:
                return True
            if length%2 != 0:
                if sub[:half+1][::-1]== sub[half:]:
                    return True
                else:
                    return False
            else:
                if sub[:half][::-1] == sub[half:]:
                    return True
                else:
                    return False  
        longest = ""
        for i in range(len(s)):
            for j in range(i+1):
                if check(s[j:i+1]):
                    if i-j+1 > len(longest):
                        longest = s[j:i+1]
        return longest