a=[5,9,4,6,7,3]
n=len(a)

for i in range(n):
    min_in=i
    for j in range(i+1,n):
        if(a[min_in] > a[j]):
            min_in=j
    a[i],a[min_in]=a[min_in],a[i]   
print(a)