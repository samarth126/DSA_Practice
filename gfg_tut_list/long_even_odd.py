a=[3,5,9,4,5,2,7,8,6,4,2,4,12]
n=len(a)
o_flag=False
e_flag=False
ln=1
if(a[0]%2 == 0):
    e_flag=True
else:
    o_flag=True

ml=1
for i in range(1,n):
    
    if(e_flag==True and a[i]%2 == 0):
        ln=0
    elif(o_flag==True and a[i]%2 != 0):
        ln=0
    else:
        ln=ln+1
    
    ml=max(ml,ln)



print(ml)