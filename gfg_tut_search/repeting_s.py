n=4
arr=[1, 2, 1, 3, 4, 3]

ls=[]
x=0
for i in range(n):
    if(arr[abs(arr[i])] > 0):
        arr[abs(arr[i])] = (-1) * arr[abs(arr[i])]
    else:
        ls.append(abs(arr[i]))
print(ls) 
