s = "3[a2[c]]"
ans = []
def decode(s:str):
    stack = []
    for i in s:
        if i!=']':
            stack.append(i)
        if i==']':
            temp = ""
            while stack[-1]!="[":
                temp = stack.pop() + temp
            stack.pop()
            num = ""
            while stack and stack[-1].isdigit():
                num =  stack.pop() + num
            stack.append(int(num)*temp)
    return "".join(stack)
print(decode(s))




