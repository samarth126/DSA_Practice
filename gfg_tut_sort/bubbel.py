a=[5,9,4,6,7,3]

for i in range(len(a)):
    for j in range((len(a)-1)-i):
        if(a[j+1] < a[j]):
            tem=a[j+1]
            a[j+1]=a[j]
            a[j]=tem
        else:
            continue
print(a)