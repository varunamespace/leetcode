L = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
     '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
def lc(digit):
    lenD,ans  = len(digit),[]
    def bfs(pos,st):
        if pos==lenD:
            ans.append(st)
        else:
            letters = L[digit[pos]]
            for letter in letters:
                bfs(pos+1,st+letter)
    bfs(0,"")
    return ans
print(lc("23"))


