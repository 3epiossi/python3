class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(1001)]
        rank = [1 for i in range(1001)]
        def find(node):
            p = par[node]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        for a, b in edges:
            if not union(a, b):
                return [a, b]