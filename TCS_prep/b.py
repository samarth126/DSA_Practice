import sys
st="aaaabbc"
dif=1
dic={}
for i in st:
    if i not in dic:
        dic[i]=1
    else:
        x=dic[i]+1
        dic[i]=x

maxi=0
mini=sys.maxsize
for i in dic:
    if(dic[i]>maxi):
        maxi=dic[i]
    if(dic[i]<mini):
        mini = dic[i]

print((maxi-mini)-dif)

