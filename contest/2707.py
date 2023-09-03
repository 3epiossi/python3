class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        length = len(s)
        dictionary = set(dictionary)
        opt = [0 for i in range(length)]
        for at in range(length):
            maxChar = opt[at-1]
            for go in range(0, at+1):
                if s[go:at+1] in dictionary:
                    maxChar = max(maxChar,(at-go+1) + opt[go-1])
            opt[at] = maxChar
        return length - opt[-1]