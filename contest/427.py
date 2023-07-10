"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
import numpy as np
class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        
        grid = np.array(grid)
        def find(center,span):
            row, col = center
            if span == 0:
                return Node(grid[row][col],1, None, None, None, None)
            curgrid = grid[row-span:row+span][::,col-span:col+span]
            stcur = set()
            stcur.update(curgrid.flatten())
            curnode = Node(0, 0, None, None, None, None)
            if 0 in stcur and 1 in stcur:
                newspan = span//2
                newinterval = ceil(span/2)
                curnode.val = 1
                curnode.isLeaf = 0
                curnode.topRight = find((row-newinterval, col+newspan), newspan)
                curnode.topLeft = find((row-newinterval, col-newinterval), newspan)
                curnode.bottomLeft = find((row+newspan, col-newinterval), newspan)
                curnode.bottomRight = find((row+newspan, col+newspan), newspan)
            else:
                curnode.val = grid[row][col]
                curnode.isLeaf = 1
            return curnode
        return find((len(grid)//2, len(grid)//2), len(grid)//2)