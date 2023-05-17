def ss(ls,n,sm):
    if n == 0:
        if sm == 0:
            return 1
        else:
            return 0
    return ss(ls,n-1,sm) + ss(ls,n-1,sm-ls[n-1])



def powerSet(ls,a):
    #code here
    print( ss(ls,len(ls),a))

powerSet([10,5,2,3,6],8)