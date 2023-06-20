"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, cur, copycur,dtpas):
        if cur in dtpas:
            return dtpas[cur]
        dtpas[cur] = copycur
        for neighbor in cur.neighbors:
            if neighbor in dtpas:
                copycur.neighbors.append(dtpas[neighbor])
                continue
            copy = Node(neighbor.val)
            copycur.neighbors.append(self.dfs(neighbor, copy, dtpas))
        return copycur
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        copyroot = Node(node.val)
        dtpas = {}
        dtpas[node] = copyroot
        for neighbor in node.neighbors:
            copy = Node(neighbor.val)
            copyroot.neighbors.append(self.dfs(neighbor, copy, dtpas))
        return copyroot
            