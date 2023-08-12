class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root
        par = root
        flag = -1
        if par.val == key:
            if par.left == None and par.right == None:
                return None
            if par.left == None:
                return par.right
            elif par.right == None:
                return par.left
            del root
            l = par.left
            r = par.right
            ptr = r
            while True:
                if l.val < ptr.val:
                    if ptr.left == None:
                        ptr.left = l
                        return r
                    ptr = ptr.left
                if l.val > ptr.val:
                    if ptr.right == None:
                        ptr.right = l
                        return r
                    ptr = ptr.right
        else:
            while True:
                LN = False
                if par.left == None:
                    LN = True
                else:
                    if par.left.val == key:
                        flag = 1
                        break
                    if par.val > key:
                        par = par.left
                        continue
                if par.right == None:
                    if LN:
                        break
                else:
                    if par.right.val == key:
                        flag = 2
                        break
                    if par.val < key:
                        par = par.right
                    else:
                        break
        if flag == -1:
            return root
        if flag == 0:
            del root
            l = par.left
            r = par.right
            ptr = r

            while True:
                if l.val < ptr.val:
                    if ptr.left == None:
                        ptr.left = l
                        return r
                    ptr = ptr.left
                if l.val > ptr.val:
                    if ptr.right == None:
                        ptr.right = l
                        return r
                    ptr = ptr.right
        if flag == 1:
            l = par.left.left
            r = par.left.right
            del par.left
            if l == None and r == None:
                par.left = None
                return root
            elif l == None:
                par.left = r
                return root
            elif r == None:
                par.left = l
                return root
            else:
                par.left = r
                ptr = r
                while True:
                    if l.val < ptr.val:
                        if ptr.left == None:
                            ptr.left = l
                            return root
                        ptr = ptr.left
                    if l.val > ptr.val:
                        if ptr.right == None:
                            ptr.right = l
                            return root
                        ptr = ptr.right
        if flag == 2:
            l = par.right.left
            r = par.right.right
            del par.right
            if l == None and r == None:
                par.right = None
                return root
            elif l == None:
                par.right = r
                return root
            elif r == None:
                par.right = l
                return root
            else:
                par.right = r
                ptr = r
                while True:
                    if l.val < ptr.val:
                        if ptr.left == None:
                            ptr.left = l
                            return root
                        ptr = ptr.left
                    if l.val > ptr.val:
                        if ptr.right == None:
                            ptr.right = l
                            return root
                        ptr = ptr.right