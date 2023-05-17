a=[2,4,6,8,10,12]
n=len(a)
key=int(input("tell no. u wanna find"))
start=0
end=int(len(a)-1)
while(start<=end):
    mid=int((start+end)/2)
    if(key==a[mid]):
        print("found at ->",mid)
        break
    if(a[mid]<key):
        start=int(mid+1)
    if(a[mid]>key):
        end=int(mid-1)


    