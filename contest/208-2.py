class TrieNode:
    def __init__(self):
        self.arrow = {}
        self.alsoLeaf = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        length = len(word)
        def dfs(ix):
            if ix >= length:
                return None
            cur = TrieNode()
            cur.arrow[word[ix]] = dfs(ix+1)
            return cur
        cur = self.root
        ix = 0
        flag = 0
        while True:
            if ix >= length:
                flag = 1
                break
            if word[ix] not in cur.arrow:
                flag = 3
                break
            if cur.arrow[word[ix]] == None:
                flag = 2
                break
            cur = cur.arrow[word[ix]]
            ix += 1
        if flag == 1:
            cur.alsoLeaf = True
            return
        if flag == 2:
            cur.arrow[word[ix]] = dfs(ix+1)
            if cur.arrow[word[ix]] != None:
                cur.arrow[word[ix]].alsoLeaf = True
            return
        if flag == 3:
            cur.arrow[word[ix]] = dfs(ix+1)
    def search(self, word: str) -> bool:
        length = len(word)
        def dfs(cur, ix):
            if ix >= length or cur == None or word[ix] not in cur.arrow:
                return False
            if ix == length-1 and\
           (cur.arrow[word[ix]] == None or\
            cur.arrow[word[ix]].alsoLeaf == True):
                return True
            return dfs(cur.arrow[word[ix]], ix+1)
        return dfs(self.root, 0)

    def startsWith(self, prefix: str) -> bool:
        length = len(prefix)
        def dfs(cur, ix):
            if ix >= length or cur == None or prefix[ix] not in cur.arrow:
                return False
            if ix == length-1 and prefix[ix] in cur.arrow:
                return True
            
            return dfs(cur.arrow[prefix[ix]], ix+1)
        
        return dfs(self.root, 0)