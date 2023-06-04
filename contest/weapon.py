"""
    find longest in one node
    find shortest in diff nodes
"""
"""
def dfs(n_time, n_condi, n_long, par):
    if len(n_condi) == 0:
        return 0
    if 
    for i in n_condi[par]:

         
    return"""
def fh(n_condi,n):

    head = [True for i in range(n)]
    index = 0
    for index in range(len(head)):
        for son in n_condi:
            if index in son:
                head[index] = False
    return head
def fl(n_time, n_condi, par):
    if len(n_condi[par]) == 0:
        return n_time[par]
    t_son = 0
    for son in n_condi[par]:
        t_son_new = fl(n_time, n_condi, son)
        if t_son < t_son_new:
            t_son = t_son_new
    return n_time[par] + t_son

T = int(input())
for i in range(T):
    n = int(input())
    n_time = list()
    n_time = list(map(int,(input().split())))
    m = int(input())
    n_condi = list()
    for j in range(n):
        n_condi.append([]) # * is use to dup index to object
    for j in range(m):
        n_input = list(map(int,input().split()))
        n_condi[n_input[1]-1].append(n_input[0]-1)
    head = fh(n_condi,n)
    tmax = 0
    for j in range(len(head)):
        if head[j] == False:
            if tmax < n_time[j]:
                tmax = n_time[j]
                continue
        t_new = fl(n_time, n_condi, j)
        if t_new > tmax:
            tmax = t_new
    print(tmax)






    
