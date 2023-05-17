# import sys
# a=[7,1,5,3,6,4]

# b_p=sys.maxsize
# m_p=0

# for i in range(0,len(a)):
#     if(b_p<a[i]):
#         m_p=max(m_p,(a[i] - b_p))
#     else:
#         b_p=a[i]


# print(m_p)

# A=[85, 30, 96, 65, 50, 8, 96, 30, 94, 24]
A=[100,180,260,310,40,535,695]
n=7
ls=[]
idx=0
for i in range(1,n):
        if(A[i-1]< A[i]):	        
            if(idx>0): 
                if(A[ls[idx-1][1]] == A[i-1]):
                    # print(A[ls[idx-1][1]])
                    ls[idx-1][1] = i-1
                    continue
        
            
            ls.append( [i-1,i] )
            idx=idx+1
	

print(ls)