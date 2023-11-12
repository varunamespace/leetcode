#Input: nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


nums = "aab"

def subs(p,nums,ans):
    if len(nums)==0:
        if p not in ans:
            ans.append(p)
        return
    first = nums[0]
    subs(p+[first],nums[1:],ans)
    subs(p,nums[1:],ans)
    return ans

print(subs([],nums,[]))
