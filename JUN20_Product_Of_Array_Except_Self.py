a = [1,2,3,4]
pl = [1 for i in range(len(a))]
pr = [1 for i in range(len(a))]
temp = 1
for i in range(len(a)):
    pl[i] = temp
    temp = temp*a[i]
print(pl)
temp = 1
for i in range(len(a)-1,-1,-1):
    pr[i] = temp
    temp = temp*a[i]
print(pr)



