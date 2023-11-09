s = "a1b2"
#s = "C"
print('a'.capitalize())

f = s[0]
ans = []
def letterCase(p,up):
    if(up==''):
        ans.append(p)
        return
    first = up[0]
    if(first.isdigit()):
        letterCase(p+first,up[1:])
    if first.isalpha():
        letterCase(p+first.capitalize(),up[1:])
        letterCase(p+first.lower(),up[1:])


#letterCase("",s)
print(ans)


a = [False]
b = "orks"
if not (a[0]):
    print(b)
