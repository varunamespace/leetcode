def partioning(p,up,ans):
    if up=="":
        check = True
        for i in p:
            check =checkPalindrome(i)
            if check==False:
                break
        if check:
            ans.append(p)
    for i in range(len(up)):
        partioning(p+[up[0:i+1]],up[i+1:],ans)
def checkPalindrome(s):
    l = 0
    r = len(s)-1
    while(l<r):
        if s[l]!=s[r]:
            return False
        l = l + 1
        r = r - 1
    return True
#s = "aab"
s = "a"
ans = []
partioning([],s,ans)
print(ans)
#print(ans)
#print(checkPalindrome("a"))