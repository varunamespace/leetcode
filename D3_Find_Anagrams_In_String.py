s = "cbaebabacd"
p = "abc"
def ana(s1,s2):


"""
def ana(s1,s2):
    n1 = len(s1)
    n2 = len(s2)
    small = min(n1,n2)
    big = max(n1,n2)
    l = []
    if small == n2:
        for i in s2:
            l.append(i)
    if small==n1:
        for i in s1:
            l.append(i)
    count= 0
    result = []
    for i in range(0,len(s1)-(small-1)):
        first = s1[i]
        if first in l:
            count = count + 1
        for j in range(i,small-1):
            j = i + 1
            if s1[j] in l:
                count = count + 1
        if count == small:
            result.append(i)
        count = 0
    print(result)

"""