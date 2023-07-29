class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ft = list(zip(*edges))
        return set(ft[0]) - set(ft[1])