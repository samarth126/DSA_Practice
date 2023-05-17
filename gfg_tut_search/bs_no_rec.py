

a=[10,4,7,3,9,2,5]
s=10
a.sort()
print(a)
n=len(a)
start=0
end=n-1
while(start <= end):
    mid=end+start // 2
    if a[mid] == s:
        print(mid)
        break
    if s > a[mid]:
        start=mid+1
    else:
        end=mid-1    