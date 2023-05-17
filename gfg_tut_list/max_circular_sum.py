a=[45,2,-4,3,-2]

# [-2,3,4,5] [3,4,5,-2] [3,4,5] [4,5,-2,3] [4,5,-2] [4,5] 

n=len(a)

# sm=0

# for i in range(n):
#     if(i>n-1):
#         i=i-(n-1)

#     for j in range(i,n):
#         print(a[i:j+1])

res=a[0]

for i in range(0,n):
    curr_max=a[i]
    curr_sum=a[i]
    for j in range(1,n):
        ind= (i+j) % n
        curr_sum= curr_sum + a[ind]

        curr_max= max(curr_max,curr_sum)
    
    res=max(res,curr_max)

print(res)
