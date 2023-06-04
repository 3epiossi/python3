"""
    jump: return value
        next h > cur
            
"""
n = int(input())
h = list()
h = list(map(int,input().split()))
v = list()
v = list(map(int,input().split()))


vmax = 0
l = 0
r = 0
for i in range(n):
    l = i
    r = l
    if vmax < v[l]:
        vmax = v[l]
    if i == n-1:
        if vmax < v[i]:
            vmax = v[i]
        break
    while True:
        if h[l] < h[r]:
            break
        if r >= n-1:
            break
        r+=1

    for m in range(l,r+1,1):
        if vmax < v[m] + v[l] and h[l] > h[m]:
            vmax = v[m] + v[l]
    
print(vmax)

