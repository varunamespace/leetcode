#can = [1,2]
#can = [2]
can = [2,3,6,7]
cd = ""
l = []
def fun(p,up,index):
    if up == 0:
        l.append(p)
        return
    for i in range(index,len(can)):
        if up-can[i]>=0:
            val = fun(p+[can[i]],up-can[i],i)
print(fun([],7,0))
print(l)
def alter(can,up,index,path,res):
    if up <0:
        return
    if up == 0:
        res.append(path)
        return
    for i in range(index,len(can)):
        alter(can,up-can[i],i,path+[can[i]],res)
