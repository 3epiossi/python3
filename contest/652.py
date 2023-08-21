# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        cache = collections.defaultdict(set)
        ans = {}
        def dfs(cur, i):
            if cur == None:
                return tuple()
            res = []
            res.extend(dfs(cur.left, i+1))
            res.append( (cur.val, i) )
            res.extend(dfs(cur.right, i+1))
            compare = tuple( map( lambda x: (x[0], x[1]-i) , res ) )
            length = len(compare)
            if compare in cache[length]:
                ans[compare] = cur
            else:
                cache[length].add(compare)
            return tuple(res)
        dfs(root, 0)
        return ans.values()