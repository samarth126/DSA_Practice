n=567

x=0

while(n>0):
    y=n%10
    n=n//10
    x=x*10
    x=x+y

print(x)