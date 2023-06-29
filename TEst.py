def decryptPassword(s):
    ans = ""
    i = 0
    stack = []
    while i < len(s):
        if s[i].isupper() and i<(len(s)-1):
            if s[i+1].islower():
                ans = ans + s[i+1] + s[i]
                i = i + 2
                continue
            else:
                ans = ans + s[i]
                i = i + 1
                continue
        if s[i] == "0":
            val = stack.pop()
            ans = ans + val
            i = i + 1
            continue
        if s[i].isdigit():
            stack.append(s[i])
            i = i + 1
            continue
        if s[i].islower():
            ans = ans + s[i]
            i = i + 1
            continue
        if s[i].isupper():
            ans = ans + s[i]
            i = i + 1
            continue
        else:
            i = i + 1
    return ans
s = "6UDTyn0Hm*BqBp*ur"
print(decryptPassword(s))
