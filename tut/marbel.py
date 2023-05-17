n=3
a=[1,9,9]

a[n-1]=a[n-1]+1

print(a)
x=0
for i in range(n-1,-1,-1):
    a[i]=x+a[i]
    if(a[i]>9):
        x=a[i]-9
    else:
        print(i+1)
        break

