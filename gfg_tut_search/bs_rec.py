
def recc(a,st,en,s):
    mid=(st+en) // 2
    # print(mid,st,en)
    if a[mid] == s:
        return mid
    if(s>a[mid]):
        return recc(a,mid+1,en,s)
    else:
        return recc(a,st,mid-1,s)
    



a=[10,4,7,3,9,2,5]
s=10
a.sort()
print(a)
n=len(a)
st=0
en=n-1
print (recc(a,st,en,s))