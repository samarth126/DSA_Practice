def pm(st, en):
    print(st," --> ",en)


def hanoi(n,st,en):
    if(n == 1):
        pm(st,en)
        return
    ot= 6 - (st+en)
    hanoi(n-1,st,ot)
    pm(st,en)
    hanoi(n-1,ot,en)

hanoi(3,1,3)