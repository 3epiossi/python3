n, m, k = tuple(map(int, input().split()))
lt_hova = list(map(int, input().split()))
dt_path = {i:[] for i in range(1,n+1)}
for i in range(m):
    s, f, v = tuple(map(int, input().split()))
    dt_path[s].append((f, v))

for now in range(k):
    dt_add = {i:0 for i in range(1,n+1)}
    for cur in dt_path:
        try:
            lt_son = list(zip(*dt_path[cur]))[0]
            lt_wei = list(zip(*dt_path[cur]))[1]
        except:
            continue
        for son in range(len(lt_son)):
            dt_add[lt_son[son]] += lt_hova[cur-1]*lt_wei[son]
    for cur in range(1,len(lt_hova)+1):
        lt_hova[cur-1] = dt_add[cur]

print(sum(lt_hova))
