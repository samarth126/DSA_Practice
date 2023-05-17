a=[1,8,30,-5,20,7]
n=len(a)
k=3

# BRUT force
# def sumk(h):
#     sumi=0
#     for i in range(h,h+k):
#         sumi=sumi+a[i]
#     return sumi


# l=0
# for i in range(n-k):
#     sumi=sumk(i)
#     l=max(l,sumi)
# print(l)


# Sliding window u can use anywhere weather product or Xor anything

curr=0
for i in range(k):
    curr = curr + a[i]
res= curr

for i in range(k,len(a)):
    curr = curr + a[i] - a[i-k]
    res=max(res,curr)
print(res)