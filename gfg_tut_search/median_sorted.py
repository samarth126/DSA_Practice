# arr1=[10,20,30,40,50]
# arr2=[5,15,25,35,45]
# arr1=[1,2,3,4,5,6]
# arr2=[10,20,30,40,50]

a1=[10,20,30]
a2=[5,15,25,35,45]

n1=len(a1) 
n2=len(a2)

b1=0
e1= n1

while(b1 <= e1):
    i1= (b1 + e1) // 2
    i2=( (n1 + n2 + 1 ) // 2) - i1

    if i1==n1:
        mnr1=float("inf")
    else:
        mnr1=a1[i1]
    
    if i1 == 0:
        mxl1=float("-inf")
    else:
        mxl1=a1[i1-1]
    
    mnr2 = a2[i2]
    mxl2 = a2[i2-1]

    if mxl1 <= mnr2 and mxl2 <= mnr1:
        if((n1 + n2) % 2 == 0):
            print( (max(mxl1,mxl2) + min(mnr1,mnr2) ) / 2 )
            break
        else:
            print( max (mxl1,mxl2) )
            break
    elif mxl1 > mnr2:
        e1 = i1 -1
    else:
        b1 = i1 +1 


