# question here is counting tyrailing zeros of a factorial there are 2 SOLUTIONS

# NAIVE SOLUTION (her will calculate factorial in different for loop and then do this to count zeros)

# x=3400
# count=0

# while(True):
#     if(x%10 == 0):
#         count=count+1
#         x=x//10
#     else:
#         break
# print(count)

# SMART SOLUTION(as only 5 and 2 can make 10 and another thing we know is that to make 10
#  u need both 5 and 2 and no. of 5 are less then the 2 so what we know here is that we 
# just need to count no. of 5 only....  )
x=5
n=5
sm=0
while(n<=x):
    y=x//n
    sm = sm+y
    n=n*5
print(sm)