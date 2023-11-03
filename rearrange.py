def maxcharm(a):
    mc = 0
    for i in range(len(a)):
        mini = a[i]
        sl = 1
        for j in range(i,len(a)):
            mini  = min(mini,a[j])
            sl = j-(i+1)
            cv = mini*sl
            mc = max(mc,cv)
    return mc
print(maxcharm([-4]))