#Input: nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [1,2,3]
l=[]
size = 3
def subs(nums,start,end):
    if(start>size or end<0):
        return
    else:
        result = nums[start:end]
        if len(result)>0:
            l.append(nums[start:end])
    subs(nums,start+1,end)
    subs(nums,start,end-1)
    print(l)
subs(nums,0,len(nums))
d