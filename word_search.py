board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = 'SEE'
#word = 'ABCCED'
word = 'ABCB'
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCS"
#board = [["A","Z"],["C","E"]]
#word = "CA"
m = len(board)
n = len(board[0])
rows, cols = (m, n)
track = [[True for i in range(cols)] for j in range(rows)]
ans = ""
def search(board,track,r,c,p,word,ans):
    if not (track[r][c]):
        return
    if len(p)==len(word):
        if p==word:
            ans = True
        track[r][c] = True
        return ans
    track[r][c] = False
    if r<len(board)-1:
        if(search(board,track,r+1,c,p+board[r+1][c],word,ans)):
           return True
    if c<len(board[0])-1:
        if(search(board, track, r, c+1, p+board[r][c+1], word,ans)):
            return True
    if r>0:
        if(search(board, track, r-1, c, p+board[r-1][c], word,ans)):
            return True
    if c>0:
        if(search(board, track, r, c-1, p+board[r][c-1], word,ans)):
            return True
    track[r][c] = True
    return
def findtheword(board,r,c,word):
    for i in range(r):
        for j in range(c):
            if board[i][j] == word[0]:
                ans = search(board,track,i,j,str(board[i][j]),word,False)
                if(ans):
                    return True
    return False

    #            if ans==True:
    #                return True
    #return False

print(findtheword(board,rows,cols,word))

#print(search(board,track,1,3,"",word,ans))
#print(ans)

