#nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
op = 4
def find(l):
    cur = 0
    ma = 0
    s = set()
    for i in l:
        s.add(i)
    for i in range(len(l)):
        if l[i]-1 not in s:
            j = l[i]
            while j in s:
                cur = cur + 1
                j = j + 1
        ma = max(ma,cur)
        cur = 0
    return ma
print(find(nums))




