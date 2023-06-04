n, m = tuple(map(int, input().split()))
lt_wt = list(map(int, input().split()))
lt_sr = []
lt_dn = []
lt_dl = []
t = 0


while True:
    if len(lt_dn) == n:
        break
    i = 0
    while len(lt_sr) != m:
        lt_sr.append(lt_wt[i])
        lt_dl.append(i)
        i += 1
    lt_dl = []
    t += 1
    temp = list(map(lambda x: x-1, lt_sr))
    lt_sr = temp
    print(lt_sr)
    for i in range(len(lt_sr)):
        if lt_sr[i] == 0:
            lt_dn.append(lt_sr[i])
            lt_dl.append(i)
    for i in lt_dl:
        del lt_sr[i]
    lt_dl = []

print(t)
