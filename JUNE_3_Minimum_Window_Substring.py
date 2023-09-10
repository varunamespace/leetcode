s = "ADOBECODEBANC"
t = "ABC"
l = []
for i in range(len(s)):
    if s[i] in t:
        l.append(i)
print(l)

