class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        dtred = {i:[] for i in range(n)}
        dtblue = {i:[] for i in range(n)}
        for edge in redEdges:
            dtred[edge[0]].append(edge[1])
        for edge in blueEdges:
            dtblue[edge[0]].append(edge[1])

        ltpas = [[0,None]]
        answer = [-1 for _ in range(n)]
        answer[0] = 0
        ltque = [[0,0,None]]
        for son in dtred[0]:
            ltque.append([son, 1, "red"])
        for son in dtblue[0]:
            ltque.append([son, 1, "blue"])

        while True:
            if ltque == []:
                break
            
            cur, dst, curcolor = ltque[0]
            del ltque[0]
            if answer[cur] == -1 and cur != 0:
                answer[cur] = dst
            ltpas.append([cur, curcolor])
            if curcolor == "red":
                for son in dtblue[cur]:
                    if [son,"blue"] not in ltpas:
                        ltque.append([son, dst+1, "blue"])

            if curcolor == "blue":
                for son in dtred[cur]:
                    if [son,"red"] not in ltpas:
                        ltque.append([son, dst+1, "red"])

        return answer