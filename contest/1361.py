class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        parent = [-1 for i in range(n)]
        pas = set()
        edges = 0
        for i in range(n):
            if leftChild[i] != -1:
                if parent[leftChild[i]] == -1 and not (leftChild[i] in pas \
                   and i in pas):
                    parent[leftChild[i]] = i
                    edges += 1
                    pas.add(leftChild[i])
                else:
                    return False
            if rightChild[i] != -1:
                if parent[rightChild[i]] == -1 and not (rightChild[i] in pas \
                   and i in pas):
                    parent[rightChild[i]] = i
                    edges += 1
                    pas.add(rightChild[i])
                else:
                    return False
            pas.add(i)
        return True if edges == n-1 else False
