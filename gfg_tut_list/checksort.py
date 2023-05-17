l=[1,87,53,56,59,68]


for i in range(0,len(l)-1):
    if(l[i]>l[i+1]):
        print("Not sorted ")
        break
else:
    print("sorted")

