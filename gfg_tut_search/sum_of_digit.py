# 2 pointer approach
# for sum of 2 digits 


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


a=[2,5,8,10,19]
n=len(a)
i=0
j=n-1
sm=21
x=sm_to(a,i,j,sm)

print(x)