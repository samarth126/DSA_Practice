a=[1,4,20,3,10,5]
n=len(a)
# sum=33

sm=a[0]
cur=33
j=0
for i in range(1,n):
    if(cur-sm == 0):
        print("true")
        break
    if(cur-sm > 0):
        sm=sm+a[i]
    if(cur-sm < 0):
        sm=sm-a[j]
        j=j+1
        



# we will be using variable sliding window here
