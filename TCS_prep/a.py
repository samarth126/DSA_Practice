s="321"
n=3
sm=0
for i in range(0,n):
    for j in range(i,n):
        # print(s[i:j+1])
        x=int(s[i:j+1])
        sm=sm + x
print(sm)