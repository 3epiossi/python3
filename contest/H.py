
T = int(input())
run = list()
for t in range(T):
    run.append(tuple(map(int,input().split())))
for t in range(T):
    D, I = run[t]
    heap = [1 for i in range(0,2**D-1)]
    id_h = 0
    for i in range(I):
        id_h = 0
        for j in range(D-1):
            if heap[id_h] == 1:
                heap[id_h] = 0
                id_h = (id_h+1)*2 -1
            else:
                heap[id_h] = 1
                id_h = (id_h+1)*2
        heap[id_h] = (0 if heap[id_h] == 1 else 1)
    heap[id_h] = (0 if heap[id_h] == 1 else 1)
    print((2*(id_h - (2**(D-1)-1)) + 1 if heap[id_h] == 1 
            else 2*(id_h -(2**(D-1)-1)) + 2))



