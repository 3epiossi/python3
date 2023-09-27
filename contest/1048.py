class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        def check(big, small):
            length1, length2 = len(big), len(small)
            if length1-length2 != 1:
                return False
            else:
                i1, i2 = 0, 0
                flag = 2
                while flag and  i1 < length1 and i2 < length2:
                    if big[i1] == small[i2]:
                        i1, i2 = i1+1, i2+1
                    else:
                        i1 += 1
                        flag -= 1
                if flag:
                    return True
                else:
                    return False
        words.sort(reverse=False, key=len)
        dp = collections.defaultdict(int)
        for word in words:
            length = 0
            for pre in dp:
                if check(word, pre):
                    length = max(dp[pre]+1, length)
            dp[word] = max(length, 1)
        return max(dp.values())
            
        