s = 'aab'
def partioning(p,up):
    if up=="":
        print(p)
    for i in range(len(up)):
        partioning(p+up[i:i+1],up[i+1:])
partioning("",s)

