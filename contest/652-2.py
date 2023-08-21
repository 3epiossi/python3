class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        cache = collections.defaultdict(set)
        ans = {}
        def dfs(cur):
            if cur == None:
                return (None, )
            res = []
            res.append(cur.val)
            res.extend( dfs(cur.left) )
            res.extend( dfs(cur.right) )
            res = tuple(res)
            length = len(res)
            if res in cache[length]:
                ans[res] = cur
            else:
                cache[length].add(res)
            return res
        dfs(root)
        return ans.values()