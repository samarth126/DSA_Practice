l=[10,20,30,40,50]
n=len(l)
i=1
p=l[0]
while(i<n):
    l[i-1]=l[i]
    i=i+1
l[n-1]=p
print(l)