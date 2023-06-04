n = int(input())
sf = list()
for i in range(n):
    sf.append(tuple(map(int, input().split())))
sf.sort(key = lambda x: x[0])
root = 0
n_gege = list()

while True:
    if root == len(sf):
        break
    n_gege.append(1)
    par = root
    while True:
        if par >= len(sf):
            break
        son = par+1
        while True:
            if son >= len(sf) or sf[son][0] >= sf[par][1]:
                break
            son += 1
        if son < len(sf):
            n_gege[-1] += 1
        par = son
    root += 1
print(max(n_gege))
