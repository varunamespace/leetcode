s = "cbaebabacd"
p = "abc"
def ana(s,p):
    sDict,pDict = {},{}
    for i in range(0,len(p)):
        sDict[s[i]] = 1 + sDict.get(s[i],0)
        pDict[p[i]] = 1 + pDict.get(p[i],0)
    if sDict==pDict:
        ans = [0]
    l = 0
    for r in range(len(p),len(s)):
        sDict[s[r]] = 1 + sDict.get(s[r],0)
        sDict[s[l]] -= 1
        if sDict[s[l]] == 0:
            sDict.pop(s[l])
        l = l + 1
        if sDict == pDict:
            ans.append(l)
    print(ans)
ana(s,p)
