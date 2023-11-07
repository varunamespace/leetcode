#obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid=[[0,0]]
count = 0
def findPath(grid,r,c,count):
    if(grid[r][c]==1):
        return 0
    if(r==(len(grid)-1) and c==(len(grid[0])-1)):
        return 1
    if r<(len(grid)-1) and c<(len(grid[0])-1):
        left = findPath(grid,r+1,c,count)
        right = findPath(grid,r,c+1,count)
        return left+right
    if r < (len(grid) - 1):
        return findPath(grid,r+1,c,count)
    if c < (len(grid[0])-1):
        return findPath(grid,r,c+1,count)

print(findPath(obstacleGrid,0,0,count))


