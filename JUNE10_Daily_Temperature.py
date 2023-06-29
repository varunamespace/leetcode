#t = [30,40,50,60]
#t = [73,74,75,71,69,72,76,73]
t = [30,60,90]
Output: [1,1,1,0]
def lis(t):
    l = []
    for i in range(0,len(t)-1):
        c = 0
        cond = False
        for j in range(i+1,len(t)):
            c+=1
            if t[j]>t[i]:
                l.append(c)
                cond = True
                break
        if not (cond):
            l.append(0)

    print(l)
lis(t)
def fun(temp):
    st = []
    res = [0]*len(temp)
    for i,t in enumerate(temp):
        while st and t>st[-1][1]:
            sti,stt = st.pop()
            res[sti] = i - sti
        st.append([i,t])
    return res
temp = [73,74,75,71,69,72,76,73]
print(fun(temp))
