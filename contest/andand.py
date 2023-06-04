def dfs(lta, ltbi, lo):
    c = 1 if ltbi[-1] == 1 else 0
    ltbi[-1] = 1 if ltbi[-1] == 0 else 0
    for i in range(len(ltbi)-2, -1, -1):
        ltbi[i], c = c ^ ltbi[i] , c & ltbi[i]
    if 1 not in ltbi:
        return lo

    ltop = list(map(lambda x, y: x*y, ltbi, lta))
    a = 2**len(ltbi)-1
    lobi = 0
    for i in range(len(ltop)):
        if ltop[i]==0:
            continue
        else:
            lobi +=1
            a = a & ltop[i]
    if lobi > lo and a != 0:
        lo = lobi
    return dfs(lta, ltbi, lo)
n = int(input())
lta = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    ltbi = [0 for i in range(n)]
    lo = 0
    lo = dfs(lta, ltbi, lo)
    print(lo)
