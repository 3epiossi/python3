class Solution:
    def minDeletions(self, s: str) -> int:
        cache = collections.defaultdict(int)
        for cur in s:
            cache[cur] += 1
        freq = list(cache.values())
        freq.sort()
        step = 0
        while len(set(freq)) != len(freq):

            for i in range(len(freq)-1):
                j = i+1
                flag = False
                if freq[j] == freq[i]:
                    while freq[j] != freq[i]: j += 1
                    freq[j-1] -= 1
                    step += 1
                    if freq[j-1] == 0:
                        del freq[j-1]

                    flag = True
                    break
                if flag == True:
                    break
        return step