#a = ["5","2","C","D","+"]
#a = ["5","-2","4","C","D","9","+","+"]
#a = ["1","C"]
def fun(a):
    stack = []
    for i in a:
        if i == "C":
            stack.pop(-1)
            continue
        if i == "D":
            last = stack[-1]
            stack.append(int(last)*1)
            continue
        if i == "+":
            prev = stack[-1]
            prev1 = stack[-2]
            stack.append(int(prev)+int(prev1))
            continue
        else:
            stack.append(int(i))
            continue
    return sum(stack)
print(fun(a))
