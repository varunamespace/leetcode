#s = "catsandog"
#l = ["cats","dog","sand","and","cat"]
s = "applepenapple"
l = ["apple","pen"]
pos = 0
"""for curword in l:
    for i in range(0,len(curword)):
        if s[pos]!=curword[i]:
            print("False")
        pos = pos+1
"""

"""
def wordBreak(s,wordDict):
    pos = 0
    cond = "true"
    for curword in wordDict:
        for i in range(0, len(curword)):
            if s[pos] != curword[i]:
                cond = "false"
                return cond
            pos = pos + 1
    return cond
print(wordBreak("catsandog",["cats","dog","sand","and","cat"]))
"""
word_dict = ["a","b","bbb","bbbb"]
string = "bb"
n = 8
dp = [True] +[False]*n
print(dp)

s = "hello"
print(s[1:3])

