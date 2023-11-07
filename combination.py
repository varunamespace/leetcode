n = 1
k = 1
res = []
ans = []
def comb(p,up,res,k):
    if len(res)==k:
        ans.append(res)
        return
    for i in range(p+1,up+1):
        comb(i,up,res+[i],k)

comb(0,n,res,k)
print(ans)


