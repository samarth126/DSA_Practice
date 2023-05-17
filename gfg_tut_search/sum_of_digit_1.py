
def sm_to(a,i,j,sm):
    while(i<j):
        cr_sm=a[i]+a[j]
        if(sm==cr_sm):
            return True
        if(cr_sm<sm):
            i=i+1
        else:
            j=j-1
    return False


a=[2,5,8,10,19,67]
n=len(a)
k=0
i=0
j=n-1
sm=35


for i in range(0,n-2):
    cr_sm = sm-a[i]
    if (sm_to(a,i+1,j,cr_sm) == True):
        print("got it")
        break
else:
    print("is not present")

    


