l=[2,3,10,6,4,8,1]
res=0
mini=l[0]
for i in range(1,len(l)):
    res = max(res, (l[i] - mini) )
    mini = min(l[i], mini)

print(res)