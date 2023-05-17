#kadans algorithm for max sum method
# in kadans if all no. are negative answer will come zero but to avoide it u can loop and check if 
# all less then just find largest _ve no. and that will be maximum

a=[-2,-3,4,-1,-2,1,5,-3]

#current sum
cs=0
#maximum sum
ms=0

for i in range(0,len(a)):
    cs=cs+a[i]
    #if cs at any point go below 0 then we will consider it as 0 only
    if(cs<0):
        cs=0
    
    if(ms<cs):
        ms=cs
print(ms)









    # ##Complete this function
    # #Function to find the sum of contiguous subarray with maximum sum.
    # def maxSubArraySum(self,arr,N):
    #     ##Your code here
    #     mx=-sys.maxsize-1
    #     x=False
    #     for i in range(N):
    #         mx=max(mx,arr[i])
    #         if(arr[i]>0):
    #             x=True
    #     if(x==False):
    #         return mx
    #     sm=0
    #     ms=0
    #     for i in range(N):
    #         sm=sm+arr[i]
    #         if(sm<0):
    #             sm=0
    #         if(ms<sm):
    #             ms=sm
        
    #     return ms




















