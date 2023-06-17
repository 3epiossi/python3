#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, ltpas, mindif):
        if root == None:
            return 10**5 + 1
        ltpas.append(root.val)
        ltcopy = []
        ltcopy.extend(ltpas)
        mindif = 10**5 + 1
        minleft = self.dfs(root.left, ltpas, mindif)
        minright = self.dfs(root.right, ltpas, mindif)
        for i in ltcopy[-2::-1]:
            a = abs(i-root.val)
            if mindif > a:
                mindif = a
        return min([minleft, minright, mindif])
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ltpas = []
        minleft = 10**5 + 1
        minright = 10**5 + 1
        mindif = 10**5 + 1
        ltpas.append(root.val)
        minleft = self.dfs(root.left, ltpas, mindif)
        minright = self.dfs(root.right, ltpas, mindif)
        return min([minleft, minright])