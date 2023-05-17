# # ans=0

# ans=0

# def rev(n):
#     if(n==0):
#         return ans
#     if(n>0):
        
#         temp=n%10
#         ans=ans*10 +temp
#         rev( n//10)
#     return ans



# print(rev(122))


# n=122
# rev=0
# while(n>0):
#     r=n%10
#     rev= rev*10+r
#     n=n//10
# print(rev)


def check(s,n,i):
    if(i==n):
        return True
    if(s[i] == s[n]):
        return 
    # s[i],s[n]=s[n],s[i]
    i=i+1
    n=n-1
    l=check(s,n,i)
    return l

a="abbcbba"
x=len(a)
print(check(a,x-1,0))
