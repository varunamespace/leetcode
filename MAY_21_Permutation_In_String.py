s1  = "ab"
s2 = "eidboaoo"
def ana(s1,s2):
    s1d = {}
    s2d = {}
    l = 0
    for i in range(len(s1)):
        s1d[s1[i]] = 1 + s1d.get(s1[i],0)
        s2d[s2[i]] = 1 + s2d.get(s2[i], 0)
    if s1d==s2d:
        return True
    for r in range(len(s1),len(s2)):
        s2d[s2[r]] = 1 + s2d.get(s2[r], 0)
        s2d[s2[l]] -= 1
        if s2d[s2[l]] == 0:
            s2d.pop(s2[l])
        l = l + 1
        if s1d==s2d:
            return True
    return False
print(ana(s1,s2))
