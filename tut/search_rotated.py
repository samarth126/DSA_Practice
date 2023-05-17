nums=[4,5,6,7,0,1,2]
t=0
start=0
end=len(nums)-1

while(start<=end):
    mid=int((start+end)/2)
    if(nums[mid]==t):
        print(mid)
        break
    
    if(nums[start] <= nums[mid]):
        if(nums[start] <= t and t <= nums[mid] ):
            end=mid-1
        else:
            start=mid+1

    else:
        if(t >= nums[mid] and t <= nums[end] ):
            start = mid+1
        else:
            end=mid-1


