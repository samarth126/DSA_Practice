def lastocc(a,x):
    n=len(a)
    st=0
    en=n-1
    while(st<=en):
        mi=(st+en) // 2

        if(a[mi] < x):
            st=mi+1
        elif(a[mi] > x):
            en=mi-1
        else:
            if mi == len(a)-1 or a[mi] != a[mi+1]:
                return mi
            else:
                st=mi+1
    return -1


ls=[5,10,10,10,10,20,20]
print(lastocc(ls,10))