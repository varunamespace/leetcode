
"""def sol(s):
    stack = []
    count = 0
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack)==0:
                continue
            else:
                stack.pop()
                count = count + 1
    return count*2
print(sol(s))
"""
def sol(s):

    stack = []
    res,ans= "",0
    for i in s:
        if len(stack)==0:
            if(i=="("):
                stack.append(i)
            else:
                res = ""
            continue
        if len(stack)>0 and i == stack[-1]:
            res = ""
            continue
        elif len(stack)==1:
            res = res + "()"
            stack.pop()
        ans = max(ans,len(res))
    print(ans)
#s = ")()())()()("
#s  = "()(()"
s =""
sol(s)


