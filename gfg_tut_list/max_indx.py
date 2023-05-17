# A = [34, 8, 10, 3, 2, 80, 30, 33, 1]
# N = 9
# N=15
# A=[65, 6, 74, 94, 56, 89, 9, 63, 75, 25, 34, 68, 93, 48, 16]

# i=1
# j=N-2
# max_ind=N-1
# mini_ind=0 
# while(mini_ind<=max_ind):
#     if(A[mini_ind] <= A[max_ind]):
#         print(max_ind-mini_ind)
#         break
#     else:
#         if(A[i]<A[mini_ind]):
#             mini_ind=i
#         if(A[j]>A[max_ind]):
#             max_ind=j
#         i=i+1
#         j=j-1


N=15
A=[65, 6, 74, 94, 56, 89, 9, 63, 75, 25, 34, 68, 93, 48, 16]

# l_m=[65, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# r_m=[94 ,94 ,94 ,94 ,93 ,93 ,93 ,93 ,93 ,93 ,93 ,93 ,93 ,48 ,16]


l_min=[0 for i in range(N)]
l_min[0]=A[0]
r_max=[0 for i in range(N)]
r_max[N-1]=A[N-1]

for i in range(1,N):
    if(A[i]<l_min[i-1]):
        l_min[i]=A[i]
    else:
        l_min[i]=l_min[i-1]

for i in range(N-2,-1,-1):
    if(r_max[i+1] < A[i] ):
        r_max[i]=A[i]
    else:
        r_max[i]=r_max[i+1]

i=0
j=0
diff=-1
while(i<N and j<N ):
    if(l_min[i] <= r_max[j]):
        diff=max(diff,j-i)
        j=j+1
    else:
        i=i+1


print(l_min)
print(r_max)

# i=1
# j=N-2
# max_ind=N-1
# mini_ind=0 
# while(mini_ind<=max_ind):
#     if(A[mini_ind] <= A[max_ind]):
#         print(max_ind-mini_ind)
#         break
#     else:
#         if(A[i]<A[mini_ind]):
#             mini_ind=i
#         if(A[j]>A[max_ind]):
#             max_ind=j
#         i=i+1
#         j=j-1


