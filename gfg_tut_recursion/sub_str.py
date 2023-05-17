# def sub_st(n,curr,i):
#     if i==len(n):
#         print(curr)
#         return 
#     sub_st(n,curr,i+1)
#     sub_st(n,curr + n[i], i+1)

def ss(s,cur,ind,fin):
    if ind == len(s):
        fin=fin +" " + cur
        return fin
    fin=ss(s,cur,ind+1,fin)
    fin=ss(s,cur + s[ind] ,ind+1,fin)
    return fin


def powerSet(s):
    #code here
    print( ss(s,"",0,""))

powerSet("abc")
# word="abcfgk"
# x=len(word)
# sub_st(word,"",0)
