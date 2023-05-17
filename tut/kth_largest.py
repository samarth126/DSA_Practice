#quick select algorithm

nums = [3,2,1,5,6,4]
k = 2
n=len(nums)-k

def quickk(l,r):
    piv=nums[r]
    p=l
    for i in range(l,r):
        if(nums[i]<piv):
            nums[p], nums[i] = nums[i], nums[p]
            p=p+1
    nums[p], nums[r] = nums[r], nums[p]

    if p>n : return quickk(l,p-1)
    if p<n : return quickk(p+1,r)
    else: return nums[p]



s=quickk(0,len(nums)-1)
print(s)