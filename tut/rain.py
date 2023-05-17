a=[4,2,0,6,3,2,5]
l_max=[0,0,0,0,0,0,0]
r_max=[0,0,0,0,0,0,0]
# first we need to find the left max and store it in an array and same with right
l_max[0]=a[0]
r_max[len(a)-1]=a[len(a)-1]

# r_end=len(a)-1

for i in range(len(a)-2,-1,-1):
    if(a[i]>r_max[i+1]):
        r_max[i]=a[i]
    else:
        r_max[i]=r_max[i+1]

for i in range(1,len(a)):
    if(a[i]>l_max[i-1]):
        l_max[i]=a[i]
    else:
        l_max[i]=l_max[i-1]

print(l_max)
print(r_max)

smm=0
for i in range(0,len(a)):
    h=min(l_max[i],r_max[i])
    smm=smm + (h-a[i])
print(smm)