l=[3,4,1,2]
# n=4
# up=0
# down=0
# for i in range(n-1):
#     if(up>0):
#         continue
#     elif(down>0):
#         continue
#     elif(l[i]<l[i+1]):
#         up=up+1
#     elif(l[i]>l[i+1]):
#         down = down+1

def rev(A,s,e):
        while(s<e):
            A[s],A[e]=A[e],A[s]
            s= s+1
            e= e-1
        return

n=3
l=[1,2,3]
up=False
do=False
rev(l,0,n-1)
print(l)
for i in range(n-1):
    if(l[i]<l[i+1] and do==True):
        break
    elif(l[i]>l[i+1] and up==True):
        break
    elif(l[i]<l[i+1]):
        up=True
    elif(l[i]>l[i+1]):
        do=True
else:
    print("nop") 
    
rev(l,0,i)
rev(l,i+1,n-1)
print(l)

i = 1
c1 = 0
c2 = 0
while(i<n):
    if l[i-1]>=l[i]:
        c1+=1
            
    if l[i-1]<=l[i]:
        c2+=1
    i+=1
        
if(c1==n-1 or c2 == n-1):
    print("yes") 
else:
    print("no")