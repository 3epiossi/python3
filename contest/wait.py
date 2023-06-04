"""
    
"""
n = int(input())
dt = dict()
lt = list()
for i in range(n):
    lt.append(tuple(map(int,input().split())))
for i in range(len(lt)):
    dt[lt[i][0]] = lt[i][1]

"""
    time++
    comming n
        wait_time_n start
    former done
         do_n start
"""
time = 0
wait_time = list()
res = list()
do_list = []
while True:
    if n == 0:
        break

    for i in range(len(wait_time)):
        wait_time[i][1]+=1

    if len(do_list):
        do_list[0] -= 1
        if(do_list[0] == 0):
            del do_list[0]
            res.append(wait_time[0])
            del wait_time[0]
            n-=1

    
    if time in dt:
        wait_time.append([time,0])
        do_list.append(dt[time])

    time+=1

ret = 0
for i in res:
    ret += i[1]

print(ret)
print(res)
