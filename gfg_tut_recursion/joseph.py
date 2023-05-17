
def josh(n,k):
    if(n==1):
        return 0
    return (josh(n-1,k) + k ) % n


print(josh(14,2))