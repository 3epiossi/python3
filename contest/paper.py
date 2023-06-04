
n = int(input())
lt = [-1 if i%2 == 0 else 1 for i in range(2**n-1)]

for i in range(n):
    id_1 = 0
    while True:
        if id_1 >= len(lt)-1:
            break
        if lt[id_1] == -1:
            id_1_1 = id_1+1
            while True:
                if id_1_1 == len(lt) or lt[id_1_1] == -1:
                    break
                id_1_1 += 1

            for k in range(id_1, id_1_1):
                if lt[k] == "U":
                    lt[k] = "D"
                elif lt[k] == "D":
                    lt[k] = "U"
                else:
                    pass
            id_1 = id_1_1+1
        else:
            id_1 += 1
    

    id_1 = 0
    for id_1 in range(len(lt)):
        if lt[id_1] == -1:
            lt[id_1] = "U"
    jump = 0
    for id1 in range(len(lt)):
        if lt[id1] == 1:
            if jump == 0:
                lt[id1] = -1
                jump =  1
            else:
                jump = 0
print(*lt)
