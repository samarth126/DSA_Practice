def sum(s):
    sumi=0
    for i in range(0,len(s)):
        sumi=sumi+s[i]
    return sumi

a=[2,4,6,8,10]
count=0
for i in range(0, len(a)):
    for j in range(i,len(a)):
        count=count+1
        print(a[i:j+1])
    print(" ")
print(count)


