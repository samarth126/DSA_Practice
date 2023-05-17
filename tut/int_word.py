n=412
a=['zero','one','two','three','four','five','six','seven','eight','nine']
def x(n):
    if(n==0):
        return ' '
    k= n%10
    l=int(n/10)
    return (x(l))
    print( a[k] )

x(n)