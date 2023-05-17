def print_pow(x,n):
    if(n == 0):
        return 1
    
    temp = print_pow(x,n//2)
    temp = temp * temp
    # elif(n == 0):

    if(n%2 == 0):
        temp = x*x
        return temp
    else:
        return temp * x
    # print(w)
    # return


x=3
n=4
print(print_pow(x,))
# y=1
# # we have to write a fun that do x ki power n 2 ki power 3 =8
# if(n<1):
#     print(1)
# else:
#     for i in range(0,n):
#         y=y*x

#     print(y)


