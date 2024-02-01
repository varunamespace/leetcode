dict = {}
up = "226"
p = ""
def comb(p,up):
    if up == "":
        print(p,up)
        return
    for i in range(len(up)):
        comb(p+up[i],up[i+1:])
comb(p,up)

