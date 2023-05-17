def cut(n,a,b,c):
    if(n==0):
        return 0
    if(n<0):
        return -1
    # x=min(a,b,c)
    res=max(cut(n-a,a,b,c),
        cut(n-b,a,b,c),
        cut(n-c,a,b,c))

    if res ==-1:
        return -1
    return res+1




a=2
b=5
c=1
n=5
print(cut(n,a,b,c))



