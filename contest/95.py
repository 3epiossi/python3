# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        cache = collections.defaultdict(list)
        def dfs(left, right):
            if right < left:
                return [None]
            if (left, right) in cache:
                return cache[(left, right)]
            ret = []
            for cur in range(left, right+1):
                leftTrees = dfs(left, cur-1)
                rightTrees = dfs(cur+1, right)
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        ret.append(TreeNode(cur, leftTree, rightTree))
            cache[(left,right)].extend(ret)
            return ret
        return dfs(1, n)