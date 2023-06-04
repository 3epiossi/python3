m, n ,k = tuple(map(int, input().split()))
ltr = list(map(int, input().split()))
ltp = list(map(int, input().split()))
pas = -1
for z2n in range(m):
    ltsc = [0 for i in range(n)]
    pas = z2n+1
    for per in range(n):
        for que in range(z2n+1):
            if ltp[per] >= ltr[que]:
                ltsc[per] += 1
    for count in range(n):
        if ltsc.count(count) > k:
            pas = -1
            break
    if pas != -1:
        print(pas)
        break
    else:
        pas = -1

if pas == -1:
    print(-1)
