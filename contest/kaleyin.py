"""
    color par
    pas par
    pair par
    leaf up
"""
def dfs(dt_path, dt_pr, lt_pas, cur, k):
    
    print(lt_pas)
    lt_pas.append(cur)
    #
    lt_cmp = []
    for son in dt_path[cur]:
        lt_cmp.append(dt_pr[son])
    color = False
    for c in range(k):
        if c not in lt_cmp:
            dt_pr[cur] = c
            color = True
            break
    if color == False:
        return False
    #
    if dt_path[cur] == []:
        return None
    if k not in dt_pr.values():
        print(dt_pr)
        return True

    for son in dt_path[cur]:
        if son not in lt_pas:
            msg = dfs(dt_path, dt_pr, lt_pas, son, k)
            if msg == None:
                continue
            if msg == True:
                return True
            if msg == False:
                continue
    return None


    return

n, m = tuple(map(int, input().split()))
k = int(input())
dt_path = {i:[] for i in range(n)}

for i in range(m):
    n1, n2 = tuple(map(int, input().split()))
    if n1 not in dt_path[n2]:
        dt_path[n2].append(n1)
    if n2 not in dt_path[n1]:
        dt_path[n1].append(n2)

root = 0
for i in dt_path:
    if len(dt_path[i])+1 == k:
        root = i
        break

dt_pr = {i:k for i in range(n)}
dt_pr[root] = 0
cur = root
lt_pas = []
for son in dt_path[cur]:
    msg = dfs(dt_path, dt_pr, lt_pas, son, k)
    if msg == True:
        break
    if msg == False:
        continue
    if msg == None:
        continue

