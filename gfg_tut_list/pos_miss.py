n = 8
a=[-7,1,2,-8,9,4,-5,5]

m=0
for i in range(n):
    if(a[i]<1):
        a[m],a[i]=a[i],a[m]
        m=m+1
print(a)
# print(m)

for i in range(n-m):
    temp=a[i+m]
    if(temp<(n-m)+1):
        a[temp+m]= -a[temp+m]

print(a)