def primee(A):
    dict = {}
    tocheck = []
    ans = []
    for i in A:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
    for i in dict:
        if dict[i]>1:
            tocheck.append(i)
    def check(n):
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    for i in tocheck:
        if(check(i)):
            ans.append(i)
    return sorted(ans)





a = [0,1,2,2,4,4,5,5,6,6]
print(primee(a))