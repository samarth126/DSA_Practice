A=[3,4,6,5]
B=[2,3,1,6]
N=4

mx=0
sq_sm=0
rt_sm=0
rt=False
for i in range(N):
    if(B[i]>=4):
        sq_sm= sq_sm + A[i]*4
        B[i]=B[i]-4
    elif(B[i]>=2):
        cur_rt_sm=A[i]*2
        print(cur_rt_sm)
        rt_sm= rt_sm + cur_rt_sm
        if(rt==False):
            rt=True
        else:
            rt=False

if(rt!=False):
    rt_sm=rt_sm-cur_rt_sm

fin=rt_sm+sq_sm

print(fin)