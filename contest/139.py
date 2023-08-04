class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = set()
        length = len(s)
        for cur in range(length):
            back = cur
            front = cur+1
            while cur-back+1 <= 20 and back >= 0:
                if s[back:front] in wordDict:
                    if back == 0:
                        cache.add(front)
                    if back in cache:
                        cache.add(front)
                back -= 1
        if length in cache:
            return True
        else:
            return False