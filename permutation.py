nums=[1,2,3]
print(nums[1:])
#p = [1]
#print(p[0:0]+[2]+p[0:])
#print(p[0:1]+[2]+p[1:])
#[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
def permutation(p,up):
    if up == []:
        print(p)
        ans.append(p)
        return
    for i in range(len(p)+1):
        f = p[0:i]
        ch = [up[0]]
        l = p[i:]
        permutation(f+ch+l,up[1:])
ans = []
permutation([],nums)

print(ans)

