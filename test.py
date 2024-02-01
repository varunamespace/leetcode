nums = [1,2,3]
l=[]
size = 3
def subs(nums):
    ans = []
    def dfs(s,path):
        ans.append(path)
        for i in range(s,len(nums)):
            dfs(i+1,path+[nums[i]])
    dfs(0,[])
    return ans
print(subs(nums))
