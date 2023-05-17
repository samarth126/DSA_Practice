# my solution

#  def isSorted(self,arr,n):
#         #code here
#         x=0
#         y=1
#         for i in range(n-1):
#             if(arr[x] != arr[y]):
#                 break
#             else:
#                 x=+1
#                 y=+1
#         else:
#             return 1
            
#         if(arr[x]>arr[y]):
#             for i in range(y,n):
#                 if(arr[i-1]<arr[i]):
#                     return 0
#         elif(arr[x]<arr[y]):
#             for i in range(y,n):
#                 if(arr[i-1]>arr[i]):
#                     return 0
#         return 1



# really effecient solution

# class Solution:
    # def isSorted(self,arr,n):
    #     #code here
    #     i = 1
    #     c1 = 0
    #     c2 = 0
    #     while(i<n):
    #         if arr[i-1]>=arr[i]:
    #             c1+=1
            
    #         if arr[i-1]<=arr[i]:
    #             c2+=1
    #         i+=1
        
    #     return (c1==n-1 or c2 == n-1)
    # # 
