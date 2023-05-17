# mergeng 2 subarray from low to mid and mid to high 

def merge1(a,low,high,mid):
    #low-mid
    #mid-high
    n1=(mid-low)+1
    n2=high-mid
    ls=[]
    i=low
    j=mid+1
    print(n1,n2,i,j)
    while(i<=mid and j<=high):
        if(a[i] <= a[j]):
            ls.append(a[i])
            i=i+1
        else:
            ls.append(a[j])
            j=j+1

    while(i<=mid):
        ls.append(a[i])
        i=i+1
    while(j<=high):
        ls.append(a[j])
        j=j+1
    x=low
    k=0
    while(x<=high):
        a[x]=ls[k]
        x=x+1
        k=k+1




a=[2,3,10,15,20,11,13,89,99]
low=2
high=6
mid=(high+low) // 2

merge1(a,low,high,mid)

print(a)









# merging 2 different arrays
# l1=[1,9,19]
# l2=[6,7,8]

# def merger(l1,l2):
#     n1=len(l1)
#     n2=len(l2)
#     l3=[]
#     i=0
#     j=0
#     while(j<n2 and i<n1):
#         if(l1[i] <= l2[j]):
#             l3.append(l1[i])
#             i=i+1
#         else:
#             l3.append(l2[j])
#             j=j+1

#     if(j>=n2):
#         x=l1[i:n1]
#         l3=l3+x
#     else:
#         x=l2[j:n2]
#         l3=l3+x
#     print(l3)

# merger(l1,l2)
