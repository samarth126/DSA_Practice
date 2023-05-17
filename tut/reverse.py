a=[2,4,6,8,10,12]
n=len(a)
start=0
end=len(a)-1
while(start<end):
    # w=a[start]
    # a[start]=a[end]
    # a[end]=w
    a[start],a[end]=a[end],a[start]
    start=start+1
    end=end-1

print(a)