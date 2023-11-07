import locale

L = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
up = "2"
p = ""

def fun(p,up):
    if up=="":
        print(p)
        return
    ch = up[0]
    length = len(L.get(ch))
    for i in range(length):
        temp = L.get(ch)
        fun(p+temp[i],up[1:])
ans = []
def funList(p,up):
    if up=="":
        return p
    ch = up[0]
    length = len(L.get(ch))
    for i in range(length):
        temp = L.get(ch)
        ans.append(funList(p+temp[i],up[1:]))
    return

fun(p,up)
print(funList(p,up))
print(ans)