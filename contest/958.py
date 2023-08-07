# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        que = [root]
        nextLevel = []
        Full = True
        while que:
            if Full == False:
                node = que.pop(0)     
                if node and (not node.left == None or not node.right == None):
                        return False
                
            else:
                node = que.pop(0)
                nextLevel.extend( (node.left,node.right) )
            if not que:
                if None in nextLevel:
                    i = 0
                    while nextLevel[i] != None: i += 1
                    if len(set(nextLevel[i:])) >= 2:
                        return False
                    else:
                        Full = False
                que.extend(nextLevel)
                nextLevel = []
        return True