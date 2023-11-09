#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = 'ABCCED'
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCB"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

m = 3
n = 4
rows, cols = (m, n)
track = [[True for i in range(cols)] for j in range(rows)]
print(track)
ans = ""
def search(board,track,r,c,p,word,ans):
    if p == word:
        ans = True
        print(ans)
        track[r][c] = False
        return
    if not (track[r][c]):
        return1
    track[r][c] = False
    if r<len(board)-1:
        search(board,track,r+1,c,p+board[r][c],word,ans)
    if c<len(board[0])-1:
        search(board, track, r, c+1, p + board[r][c], word,ans)
    if r>0:
        search(board, track, r-1, c, p + board[r][c], word,ans)
    if c>0:
        search(board, track, r, c-1, p + board[r][c], word,ans)
    track[r][c] = True
search(board,track,0,0,"",word,ans)
print(ans)

