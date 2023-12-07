height = [1,8,6,2,5,4,8,3,7]
#ans = 49

def maxwater(height):
    l = 0
    r  = len(height)-1
    maxi = 0
    while l<r:
        h = min(height[l],height[r])
        w = (r-l)
        maxi = max(maxi,h*w)
        if l<r:
            l = l +1
        if r<l:
            r = r - 1
    return maxi
print(maxwater(height))

