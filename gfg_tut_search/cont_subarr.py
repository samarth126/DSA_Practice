def subArraySum(arr, n, s): 
    #Write your code here
    i=0
    j=0
    cr_sm=arr[i]
    while(n>j and n>i):
        if(cr_sm == s):
            return i,j
        elif(cr_sm < s):
            print(j)
            j+1
            cr_sm = cr_sm + arr[j]
        else:
            print(i)
            i=i+1
            cr_sm = cr_sm - arr[i]
    return -1

print(subArraySum([1,2,3,5,7], 5, 12)) 