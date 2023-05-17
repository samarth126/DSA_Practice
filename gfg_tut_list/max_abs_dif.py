arr=[2,4,8,7,7,9,3]
n=len(arr)
mini =0
l_d=[0 for i in range(len(arr))]
r_d=[0 for i in range(len(arr))]
for i in range(0,n):
    if(arr[i]< mini):
        l_d[i]=mini
        mini=arr[i]
    elif(arr[i]< mini):
        l_d[i]=mini

print(l_d)
print(r_d)