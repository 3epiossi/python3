"""
    each path max charge
    two path compare min charge(sf same)
"""
def dfs(adj, lt_pas, dt_min, parmax, root, par, end):
    if par in lt_pas or adj[par] == []:
        return
    if par == end:
        if parmax < dt_min[(root, end)]:
            dt_min[(root, end)] = parmax
        return
    for son in adj[par]:
        lt_pas.append(par)
        dfs(adj, lt_pas, dt_min, max([son[1], parmax]), root, son[0], end)
        lt_pas.remove(par)
    return
n, nn = tuple(map(int, input().split()))
lt_path = []
lta = []
ltb = []
ltv = []
for i in range(nn):
    a, b, v = tuple(map(int, input().split()))
    lta.append(a)
    ltb.append(b)
    ltv.append(v)
lt_path.extend(tuple(zip(lta, ltb, ltv)))
lt_path.extend(tuple(zip(ltb, lta, ltv)))
lt_path.sort(key = lambda x:x[0])

path = []
for i in range(n):
    path.append([])
adj = {i:[] for i in range(n)}
while True:
    lt = list(zip(*lt_path))
    for j in range(n):
        id_s = lt[0].index(j)
        id_f = len(lt[0])-1-lt[0][::-1].index(j)
        path[j].extend(list(zip(lt[0][id_s:id_f+1],lt[1][id_s: id_f+1], lt[2][id_s:id_f+1])))
    break
for i in range(len(path)):
    for j in range(len(path[i])):
        adj[i].append( (path[i][j][1], path[i][j][2]) )


lt_rec = []
for i in range(n):
    lt_rec.append([])

dt_min = {}
for root in adj:
    par = root
    for end in range(n):
        if end == root:
            continue
        dt_min[(root, end)] = 2**31-1
        parmax = 0
        lt_pas = []
        dfs(adj, lt_pas, dt_min, parmax,  root, par, end)

print(max(dt_min.values()))
print(*dt_min)

