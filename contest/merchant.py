n = int(input())
dlt_pt = []
for i  in range(n):
    dlt_pt.append(tuple(map(int, input().split())))

dlt_pt.sort(key = lambda x:x[0])

ymin, ymax = min(list(zip(*dlt_pt))[1]) ,max(list(zip(*dlt_pt))[1])

peomin, rotmin = 2**31-1, 2**31-1

for peoy in range(ymin, ymax+1):
    peox= dlt_pt[0][0]
    peov, rotv = 0, 0
    for tp_pt in dlt_pt:
        peov += 2*(tp_pt[0]-peox)
        rotv += 2*abs(peoy - tp_pt[1])
        peox = tp_pt[0]
    if peomin > peov:
        peomin = peov
    if rotmin > rotv:
        rotmin = rotv
print(f'{peomin} {rotmin}')


