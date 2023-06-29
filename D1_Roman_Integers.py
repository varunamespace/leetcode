#a = 'III'
a = 'IV'
dict = {'I':1,'V':5,'L':50}
s = 0
l = len(a)
for i in range(l-1):
    if dict[a[i]]<dict[a[i+1]]:
        s = s - dict[a[i]]
    else:
        s = s + dict[a[i]]
print(s+dict[a[-1]])


