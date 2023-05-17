# l=[1,5,3,1,2,8]
# n=len(l)

# sm=0
# for i in range(1,n):
#     if(l[i] > l[i-1]):
#         sm = sm + l[i]-l[i-1]

# print(sm)

l=[1,5,3,1,2,8]
n=len(l)
idx=0
ls=[]
for i in range(1,n):
    if(l[i] > l[i-1]):
        if(idx>0):
            if (ls[idx-1][1] == i-1):
                ls[idx-1][1]=i
                continue
        ls.append([i-1, i])
        idx=idx+1

# for i in range(1,len(ls)):
#     if (ls[i-1][1] == ls[i][0]):
#         ls[i-1][1]= ls[i][1]
#         ls.pop(i)

print(ls)
  