def sum(s):
    sumi=0
    for i in range(0,len(s)):
        sumi=sumi+s[i]
    return sumi



a=[1,-2,6,-1,3]
count=0
l=0

for i in range(0, len(a)):
    for j in range(i,len(a)):
        count=count+1
        x=a[i:j+1]
        print(x)
        sm=sum(x)
        if(sm>l):
            l=sm
        
    print(" ")
print(count)
print(l)


