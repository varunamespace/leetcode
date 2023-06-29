def decodeString(s: str) -> str:
    stack = []  # (prevStr, repeatCount)
    currStr = ''
    currNum = 0
    for c in s:
      if c.isdigit():
        currNum = currNum * 10 + int(c)
      else:
        if c == '[':
          stack.append((currStr, currNum))
          currStr = ''
          currNum = 0
        elif c == ']':
          prevStr, num = stack.pop()
          currStr = prevStr + num * currStr
        else:
          currStr += c

    return currStr
#s = '3[a2[c]]'
s = '3[a]2[bc]aa'
print(decodeString(s))



"""def decode(s):
    curnum = 0
    curstr = ""
    stack = []
    for i in s:
        if i.isdigit():
            curnum = curnum*10+int(i)
        else:
            if i=='[':
                stack.append((curstr,curnum))
                curstr = ""
                curnum = 0
            elif i==']':
                prevstr,prevnum = stack.pop()
                curstr = prevstr+prevnum*curstr
            else:
                curstr = curstr + i
    return curstr
s = "3[a]2[bc]"
print(decode(s))"""