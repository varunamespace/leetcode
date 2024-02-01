nums = [-1,0,3,5,9,12]
target = 9
def bin(l,start,end,tar):
    if(start>end):
        return False
    else:
        mid = (start+end)//2
        if l[mid]==tar:
            return mid
        elif tar >=l[mid]:
            return bin(l,mid+1,end,tar)
        else:
            return bin(l,start,mid-1,tar)
print(bin(nums,0,len(nums),9))
